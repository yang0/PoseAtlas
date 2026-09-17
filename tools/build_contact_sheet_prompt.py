#!/usr/bin/env python3
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
poses={x['id']:x for x in json.loads((ROOT/'data/poses.json').read_text(encoding='utf-8'))['items']}
pages=json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8'))['items']
p=argparse.ArgumentParser()
p.add_argument('--category',required=True,choices=['ST','SI','KN','SQ','FL','LE','WK','MV'])
p.add_argument('--page',required=True,type=int)
a=p.parse_args()
page=next((x for x in pages if x['category']==a.category and x['category_page']==a.page),None)
if not page: raise SystemExit('page not found')
print(f"Create one 4x4 Pose Atlas contact sheet titled: {page['title']}")
print("Same adult model, same neutral fitted outfit, neutral gray seamless studio, even light, full body, hands and feet visible. Exactly 16 cells. Each cell must obey the canonical pose definition below. Put only the exact Pose ID under each cell. JSON is authoritative; do not infer pose meaning from prior generated sheets.\\n")
for i,pid in enumerate(page['pose_ids'],1):
    x=poses[pid]
    print(f"{i}. {pid} | {x['name_zh']} | {x['summary']} | support={x['support']['description']} | legs={x['legs']} | weight={x['weight']} | pelvis={x['pelvis']} | torso={x['torso']} | shoulders={x['shoulders']} | shape={x['shape']['primary']} | intensity={x['intensity']}")
