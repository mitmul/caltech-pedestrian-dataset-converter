#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import json
from scipy.io import loadmat
from collections import defaultdict

all_obj = 0
data = defaultdict(dict)
for dname in sorted(glob.glob('data/annotations/set*')):
    set_name = os.path.basename(dname)
    data[set_name] = defaultdict(dict)
    for anno_fn in sorted(glob.glob('{}/*.vbb'.format(dname))):
        vbb = loadmat(anno_fn)
        nFrame = int(vbb['A'][0][0][0][0][0])
        objLists = vbb['A'][0][0][1][0]
        maxObj = int(vbb['A'][0][0][2][0][0])
        objInit = vbb['A'][0][0][3][0]
        objLbl = [str(v[0]) for v in vbb['A'][0][0][4][0]]
        objStr = vbb['A'][0][0][5][0]
        objEnd = vbb['A'][0][0][6][0]
        objHide = vbb['A'][0][0][7][0]
        altered = int(vbb['A'][0][0][8][0][0])
        log = vbb['A'][0][0][9][0]
        logLen = int(vbb['A'][0][0][10][0][0])

        video_name = os.path.splitext(os.path.basename(anno_fn))[0]
        data[set_name][video_name]['nFrame'] = nFrame
        data[set_name][video_name]['maxObj'] = maxObj
        data[set_name][video_name]['log'] = log.tolist()
        data[set_name][video_name]['logLen'] = logLen
        data[set_name][video_name]['altered'] = altered
        data[set_name][video_name]['frames'] = defaultdict(list)

        n_obj = 0
        for frame_id, obj in enumerate(objLists):
            if len(obj) > 0:
                for id, pos, occl, lock, posv in zip(
                        obj['id'][0], obj['pos'][0], obj['occl'][0],
                        obj['lock'][0], obj['posv'][0]):
                    keys = obj.dtype.names
                    id = int(id[0][0]) - 1  # MATLAB is 1-origin
                    pos = pos[0].tolist()
                    occl = int(occl[0][0])
                    lock = int(lock[0][0])
                    posv = posv[0].tolist()

                    datum = dict(zip(keys, [id, pos, occl, lock, posv]))
                    datum['lbl'] = str(objLbl[datum['id']])
                    datum['str'] = int(objStr[datum['id']])
                    datum['end'] = int(objEnd[datum['id']])
                    datum['hide'] = int(objHide[datum['id']])
                    datum['init'] = int(objInit[datum['id']])
                    data[set_name][video_name][
                        'frames'][frame_id].append(datum)
                    n_obj += 1

        print(dname, anno_fn, n_obj)
        all_obj += n_obj

print('Number of objects:', all_obj)
json.dump(data, open('data/annotations.json', 'w'))
