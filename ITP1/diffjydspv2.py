
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

    before_params = dividing('/Users/icko/Documents/000/yjdspv2/stg/adprodsetbetabefore8211930')
    after_params = dividing('/Users/icko/Documents/000/yjdspv2/stg/adprodsetbetaafter8211930')

    for k in set(before_params.keys()) - set(after_params.keys()):
        print('[Caution] ' + k + ' vanished!')

    for k in set(after_params.keys()) - set(before_params.keys()):
        print('[Info] ' + k + ' is added!')

    for v in before_params.keys():
        before_obj = before_params[v]['params']
        after_obj = after_params[v]['params']

        if 'api_timeout' not in before_obj.keys() and after_obj['api_timeout'] == '0':
            print("adprodset_code " + v + " api_timeout [key] not exists in params but equals '0' in Table ds_adprodset_Yjdspv2")
            continue
        if before_obj['creative_options'] == after_obj['creative_options'] and before_obj['height'] == after_obj['height'] and \
                before_obj['width'] == after_obj['width'] and before_obj['callback'] == after_obj['callback'] and \
                before_obj['id'] == after_obj['id'] and before_obj['js_file'] == after_obj['js_file'] and \
                (before_obj['api_timeout'] == after_obj['api_timeout'] or (before_obj['api_timeout'] == '' and after_obj['api_timeout'] == '0')) and \
                before_obj['position'] == after_obj['position']:
            print('Product [Yjdspv2] is no problem')
        else:
            if before_obj['creative_options'] != after_obj['creative_options']:
                print('creative_options in adprodset_code ' + v + ' is different')
            else:
                print(v + ' creative_options is OK')
            if before_obj['width'] != after_obj['width']:
                print('width in adprodset_code ' + v + ' is different')
            else:
                print(v + ' width is OK')
            if before_obj['height'] != after_obj['height']:
                print('height in adprodset_code ' + v + ' is different')
            else:
                print(v + ' Height is OK')
            if before_obj['id'] != after_obj['id']:
                print('id in adprodset_code ' + v + ' is different')
            else:
                print(v + ' zone_id is OK')
            if before_obj['callback'] != after_obj['callback']:
                print('callback in adprodset_code ' + v + ' is different')
            else:
                print(v + ' callback is OK')
            if before_obj['js_file'] != after_obj['js_file']:
                print('js_file in adprodset_code ' + v + ' is different')
            else:
                print(v + ' js_file is OK')
            if before_obj['position'] != after_obj['position']:
                print('position in adprodset_code ' + v + ' is different')
            else:
                print(v + ' position is OK')