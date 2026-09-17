#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/poses.json').read_text(encoding='utf-8'))
items=d['items']; expected={'ST':112,'SI':64,'KN':64,'SQ':48,'FL':64,'LE':48,'WK':32,'MV':48}
err=[]
ids=[x['id'] for x in items]
if len(items)!=480: err.append(f'pose count {len(items)} != 480')
if len(set(ids))!=len(ids): err.append('duplicate IDs')
for cat,n in expected.items():
    got=sum(1 for x in items if x['category']==cat)
    if got!=n: err.append(f'{cat}: {got} != {n}')
for x in items:
    if not re.match(r'^(ST|SI|KN|SQ|FL|LE|WK|MV)-\d{3}$',x['id']): err.append('bad id '+x['id'])
    if not 1<=x.get('intensity',0)<=5: err.append('bad intensity '+x['id'])
    if len(x.get('variants',[]))!=3: err.append('bad variants '+x['id'])
    if x.get('image')!=f"assets/pose-images/{x['id']}.webp": err.append('bad image path '+x['id'])
v=json.loads((ROOT/'data/variants.json').read_text(encoding='utf-8'))
if len(v['items'])!=1440: err.append('variant count != 1440')
p=json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8'))
if len(p['items'])!=30: err.append('page count != 30')
for pg in p['items']:
    if len(pg['pose_ids'])!=16: err.append('page not 16 '+pg['page_id'])
    cats={poses.split('-')[0] for poses in pg['pose_ids']}
    if len(cats)!=1: err.append('mixed category '+pg['page_id'])
if err:
    print('\n'.join(err)); sys.exit(1)
print('OK: 480 pose families, 1440 variants, 30 contact-sheet pages; category counts and ID paths valid.')
