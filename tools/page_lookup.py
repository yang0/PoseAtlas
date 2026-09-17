#!/usr/bin/env python3
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
pages = json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8'))['items']
poses = {x['id']: x for x in json.loads((ROOT/'data/poses.json').read_text(encoding='utf-8'))['items']}

p = argparse.ArgumentParser(description='Lookup page / pose / category and return mapped image paths')
g = p.add_mutually_exclusive_group(required=True)
g.add_argument('--page-id')
g.add_argument('--pose-id')
g.add_argument('--category', choices=['ST','SI','KN','SQ','FL','LE','WK','MV'])
a = p.parse_args()

if a.page_id:
    hit = next((x for x in pages if x['page_id'] == a.page_id), None)
    if not hit: raise SystemExit('page not found')
    print(json.dumps(hit, ensure_ascii=False, indent=2))
elif a.pose_id:
    hit = next((x for x in pages if a.pose_id in x['pose_ids']), None)
    if not hit: raise SystemExit('pose not found')
    out = {
      'pose_id': a.pose_id,
      'pose_name_zh': poses[a.pose_id].get('name_zh'),
      'page_id': hit['page_id'],
      'title': hit['title'],
      'category': hit['category'],
      'category_page': hit['category_page'],
      'image_path': hit.get('image_path', hit.get('output_hint')),
      'image_png_path': hit.get('image_png_path'),
      'pose_index_in_page': hit['pose_ids'].index(a.pose_id) + 1,
      'pose_range': f"{hit['pose_ids'][0]}–{hit['pose_ids'][-1]}"
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
else:
    hits = [x for x in pages if x['category'] == a.category]
    out = [{
      'page_id': x['page_id'],
      'title': x['title'],
      'pose_range': f"{x['pose_ids'][0]}–{x['pose_ids'][-1]}",
      'image_path': x.get('image_path', x.get('output_hint')),
      'image_png_path': x.get('image_png_path')
    } for x in hits]
    print(json.dumps(out, ensure_ascii=False, indent=2))
