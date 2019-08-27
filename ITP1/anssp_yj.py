if __name__ == '__main__':
    # yjdspv2
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
            if len(data) != 0 and data['adprod_type'] == '10':

                subdata = data['adprod_params']
                c = subdata.split('')
                params = {}
                for j in c:
                    d = j.split('')
                    params[d[0]] = d[1]
                result[adprodset_code.strip('\n')] = {'params': params}
        return result

    before_params = dividing('/Users/icko/Documents/000/yjdspv2/stg/adprodsetprodbefore8261600')
    after_params = dividing('/Users/icko/Documents/000/yjdspv2/stg/adprodsetprodafter8261600')

    for k in set(before_params.keys()) - set(after_params.keys()):
        print('[Caution] ' + k + ' vanished!')

    for k in set(after_params.keys()) - set(before_params.keys()):
        print('[Info] ' + k + ' is added!')

    for i, v in enumerate(before_params.keys()) and enumerate(after_params.keys()):
        before_obj = before_params[v]['params']
        after_obj = after_params[v]['params']

        if 'api_timeout' not in before_obj.keys() and after_obj['api_timeout'] == '0':
            print("adprodset_code " + v + " api_timeout [key] not exists in params but equals '0' in Table ds_adprodset_anssp_yj")
            continue

        if before_obj['creative_options'] != after_obj['creative_options']:
            print('creative_options in adprodset_code ' + v + ' is different')
        elif before_obj['width'] != after_obj['width']:
            print('width in adprodset_code ' + v + ' is different')
        elif before_obj['height'] != after_obj['height']:
            print('height in adprodset_code ' + v + ' is different')
        elif before_obj['id'] != after_obj['id']:
            print('id in adprodset_code ' + v + ' is different')
        elif before_obj['callback'] != after_obj['callback']:
            print('callback in adprodset_code ' + v + ' is different')
        elif before_obj['js_file'] != after_obj['js_file']:
            print('js_file in adprodset_code ' + v + ' is different')
        elif before_obj['position'] != after_obj['position']:
            print('position in adprodset_code ' + v + ' is different')
        elif 'member' in before_obj.keys() and'member' in after_obj.keys():
            if before_obj['member'] != after_obj['member']:
                print('member in adprodset_cod' + v + ' is different')
    print('*********************************')
    print('*', i+1, "[YJDSPv2] products are OK", '*')
    print('*********************************')

