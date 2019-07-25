
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

    before_params = dividing('/Users/icko/Documents/000/anssp/adprodsetprodbefore7241200')
    after_params = dividing('/Users/icko/Documents/000/anssp/adprodsetprodafter7241200')

    for k in set(before_params.keys()) - set(after_params.keys()):
        print('[Caution] ' + k + ' vanished!')

    for k in set(after_params.keys()) - set(before_params.keys()):
        print('[Info] ' + k + ' is added!')

    for v in before_params.keys():
        before_obj = before_params[v]['params']
        after_obj = after_params[v]['params']

        if before_obj == after_obj:
            print('Product [Anssp] is no problem')
        else:
            if before_obj['position'] != after_obj['position']:
                print('Position in adprodset_code ' + v + ' is different')
            else:
                print(v + ' Position is OK')
            if 'width' not in before_obj.keys() or 'height' not in before_obj.keys():
                print(v + ' width,height [key] is not exist\n')
                continue
            if before_obj['width'] != after_obj['width']:
                print('Width in adprodset_code ' + v + ' is different')
            else:
                print(v + ' Width is OK')

            if before_obj['height'] != after_obj['height']:
                print('Width in adprodset_code ' + v + ' is different')
            else:
                print(v + ' Height is OK')