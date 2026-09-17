#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
poses=json.loads((ROOT/'data/poses.json').read_text(encoding='utf-8'))['items']
missing=[x['id'] for x in poses if not (ROOT/x['image']).exists()]
print(f'canonical images present: {len(poses)-len(missing)}/{len(poses)}')
if missing:
    print('missing first 30:', ', '.join(missing[:30]))
