
if __name__ == '__main__':
# anssp
    def dividing(file_name):
        result = {}
        all_lines = open(file_name).readlines()
        for line in all_lines:
            data = {}
            a = line.split('')
            if len(a) <= 1:
                adprodset_code = line.strip()
                continue
            for i in a:
                b = i.split('')
                data[b[0]] = b[1]
            if len(data) != 0 and data['adprod_type'] == '12':

                subdata = data['adprod_params']
                c = subdata.split('')
                params = {}
                for j in c:
                    d = j.split('')
                    params[d[0]] = d[1]
                result[adprodset_code.strip('\n')] = {'params': params}
        return result

    before_params = dividing('/Users/icko/Documents/000/anssp/release-stg/adprodsetbetaprod')
    after_params = dividing('/Users/icko/Documents/000/anssp/release-stg/adprodsetbetastg')

    for k in set(before_params.keys()) - set(after_params.keys()):
        print('[Caution] ' + k + ' vanished!')

    for k in set(after_params.keys()) - set(before_params.keys()):
        print('[Info] ' + k + ' is added!')

    for v in before_params.keys():
        before_obj = before_params[v]['params']
        after_obj = after_params[v]['params']

        if before_obj['position'] == after_obj['position'] and before_obj['height'] == after_obj['height'] and \
                before_obj['width'] == after_obj['width'] and before_obj['id'] == after_obj['id']:
            print('Product [Anssp] is no problem')
        else:
            if before_obj['position'] != after_obj['position']:
                print('Position in adprodset_code ' + v + ' is different')
            else:
                print(v + ' Position is OK')
            if before_obj['width'] != after_obj['width']:
                print('Width in adprodset_code ' + v + ' is different')
            else:
                print(v + ' Width is OK')

            if before_obj['height'] != after_obj['height']:
                print('Width in adprodset_code ' + v + ' is different')
            else:
                print(v + ' Height is OK')
            if before_obj['id'] != after_obj['id']:
                print('id in adprodset_code ' + v + ' is different')
            else:
                print(v + ' id is OK')