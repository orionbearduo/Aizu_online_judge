from collections import OrderedDict
import subprocess
import json
import re

class Mdbm(OrderedDict):
    def __init__(self, filename, valuetype = 'json'):
        super(Mdbm, self).__init__()
        cmd = ['/home/y/bin64/mdbm_export', '-c', filename]
        cdbdump = subprocess.check_output(cmd, universal_newlines=True)
        if valuetype == 'control':
            for line in cdbdump.split('\n'):
                tmp = line.split(':', 1)
                if len(tmp) < 2:
                    return
                key, value = tmp[1].strip().split('->', 1)
                value = re.sub('\', '\', value)
                value = re.sub('\', '\', value)
                value = re.sub('\', '\', value)
                value = re.sub('\', '\', value)
                data = {}
                for r in value.split('\'):
                    s = r.split('\');
                    if len(s) == 2:
                        data[s[0]] = s[1]
                self[key] = data
        elif valuetype == 'json':
            for line in cdbdump.split('\n'):
                tmp = line.split(':', 1)
                if len(tmp) < 2:
                    return
                key, value = tmp[1].strip().split('->', 1)
                data = json.loads(value)
                self[key] = data

def check(old_path, new_path, frame_path):
    old_m = Mdbm(old_path, 'control')
    new_m = Mdbm(new_path, 'control')
    frame_m = Mdbm(frame_path)

    # common
    for k in set(old_m.keys()) & set(new_m.keys()):
        # different value
        if old_m[k] != new_m[k]:
            # frame_id vanished
            if 'frame_id' in old_m[k] and 'frame_id' not in new_m[k]:
                frame_id = old_m[k]['frame_id']
                if 'uso' in frame_m[frame_id]:
                    print('[warn] Adframe ' + k + ' has got out!')
                else:
                    print('[info] Old frame ' + k + ' has got out!')
            else:
                print('[warn] the value of ' + k + ' has changed! (not frame_id)')
                print(old_m[k])
                print(new_m[k])

    # old only
    for k in set(old_m.keys()) - set(new_m.keys()):
        print('[warn] ' + k + ' vanished!')

    # new only
    for k in set(new_m.keys()) - set(old_m.keys()):
        print('[info] ' + k + ' is added!')

if __name__ == '__main__':
    print('1. check test/adprodset.mdbm')
    check('./anemos-partner-yads/test/adprodset.mdbm', './anemos-partner-yads-staging/test/adprodset.mdbm', './anemos-partner-yads/test/frame.mdbm')

    print()

    print('2. check prod/adprodset.mdbm')
    check('./anemos-partner-yads/prod/adprodset.mdbm', './anemos-partner-yads-staging/prod/adprodset.mdbm', './anemos-partner-yads/prod/frame.mdbm')
