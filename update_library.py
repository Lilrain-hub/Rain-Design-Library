#!/usr/bin/env python3
"""Validate resources.json and rebuild the offline HTML and CSV (stdlib only)."""
import argparse
import csv
import io
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
COLUMNS = ['id', 'name', 'category', 'url', 'license_url', 'access', 'license',
           'grade', 'html_friendly', 'react_friendly', 'tech', 'tags', 'use',
           'priority', 'description']


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def web_url(value):
    if not isinstance(value, str):
        raise ValueError('URL must be text')
    p = urlparse(value)
    if p.scheme != 'https' or not p.hostname or p.username or p.password:
        raise ValueError('Expected an HTTPS URL without credentials: ' + value)


def build():
    data = read_json('resources.json')
    meta = read_json('catalog-meta.json')
    reviews = read_json('reviews.json')
    if not isinstance(data, list) or not data:
        raise ValueError('resources.json must be a nonempty array')
    updated = date.fromisoformat(meta['updated_at'])
    if updated > date.today():
        raise ValueError('Content update date is in the future')
    if type(meta['new_count']) is not int or not 0 <= meta['new_count'] <= len(data):
        raise ValueError('Invalid new_count')
    ids = set()
    legacy_ids = set(meta['legacy_ids'])
    urls = set()
    for item in data:
        rid = item.get('id', '')
        if not re.fullmatch(r'R[0-9]{2,}', rid) or rid in ids:
            raise ValueError('Invalid or duplicate id: ' + rid)
        ids.add(rid)
        for field in COLUMNS:
            if field not in item:
                raise ValueError(f'{rid}: missing {field}')
        for field in ['name', 'category', 'access', 'license', 'tech', 'use', 'description']:
            if not isinstance(item[field], str) or not item[field].strip():
                raise ValueError(f'{rid}: empty {field}')
        for field in ['url', 'license_url']:
            web_url(item[field])
        normalized = item['url'].rstrip('/').lower()
        if normalized in urls:
            raise ValueError(f'{rid}: duplicate URL')
        urls.add(normalized)
        if item['grade'] not in ('A', 'B', 'C', 'D'):
            raise ValueError(f'{rid}: invalid grade')
        if any(type(item[k]) is not bool for k in ['html_friendly', 'react_friendly']):
            raise ValueError(f'{rid}: compatibility flags must be booleans')
        if type(item['priority']) is not int or not 1 <= item['priority'] <= 5:
            raise ValueError(f'{rid}: priority must be 1–5')
        if not isinstance(item['tags'], list) or not all(isinstance(t, str) for t in item['tags']):
            raise ValueError(f'{rid}: tags must be an array of text')
        if rid not in legacy_ids:
            review = reviews.get(rid, {})
            if item['grade'] not in ('A', 'B'):
                raise ValueError(f'{rid}: weekly additions must be verified free resources')
            for field in ['verified_at', 'free_scope', 'license_summary', 'official_sources']:
                if not review.get(field):
                    raise ValueError(f'{rid}: missing review evidence {field}')
            checked = date.fromisoformat(review['verified_at'])
            if checked > updated:
                raise ValueError(f'{rid}: review is later than content update')
            if not isinstance(review['official_sources'], list):
                raise ValueError(f'{rid}: official_sources must be an array')
            for url in review['official_sources']:
                web_url(url)

    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    # Escape script terminators and line separator characters in external descriptions.
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    payload = payload.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    html, n = re.subn(r'const DATA=.*?;(?=\s*const \$=)', lambda _: 'const DATA=' + payload + ';', html, flags=re.S)
    if n != 1:
        raise ValueError('Could not find exactly one embedded DATA array')
    html = re.sub(r'<title>.*?</title>', f'<title>Rain Design Library · {len(data)} 个网页素材来源</title>', html)
    html = re.sub(r'(<strong id="total">).*?(</strong>)', lambda m: m[1] + str(len(data)) + m[2], html)
    html = re.sub(r'(<strong id="new">).*?(</strong>)', lambda m: m[1] + '+' + str(meta['new_count']) + m[2], html)
    html = re.sub(r'(<div class="footer">).*?(</div>)', lambda m: m[1] + f'Rain Design Library · 内容更新 {updated} · v2.0 · 在线与离线共用同一份资源索引' + m[2], html)
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=COLUMNS, lineterminator='\n')
    writer.writeheader()
    for item in data:
        row = {k: item[k] for k in COLUMNS}
        row['tags'] = '、'.join(row['tags'])
        writer.writerow(row)
    return {'index.html': html.encode('utf-8'),
            'resources.csv': ('\ufeff' + stream.getvalue()).encode('utf-8')}, len(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if generated files are stale')
    args = parser.parse_args()
    outputs, count = build()
    stale = [name for name, content in outputs.items() if (ROOT / name).read_bytes() != content]
    if args.check:
        if stale:
            raise SystemExit('Generated files are stale: ' + ', '.join(stale))
        print(f'OK: {count} resources; CSV and HTML match JSON; review evidence validated')
    else:
        for name, content in outputs.items():
            if name in stale:
                (ROOT / name).write_bytes(content)
        print(f'Synced {count} resources: ' + (', '.join(stale) or 'already current'))


if __name__ == '__main__':
    main()
