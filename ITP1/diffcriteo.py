
if __name__ == '__main__':
# criteo
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
            if len(data) != 0 and data['adprod_type'] == '4':

                subdata = data['adprod_params']
                c = subdata.split('')
                params = {}
                for j in c:
                    d = j.split('')
                    params[d[0]] = d[1]
                result[adprodset_code.strip('\n')] = {'params': params}
        return result

    before_params = dividing('/Users/icko/Documents/000/criteo/stg/adprodsetbetabefore8161645')
    after_params = dividing('/Users/icko/Documents/000/criteo/stg/adprodsetbetaafter8161645')

    for k in set(before_params.keys()) - set(after_params.keys()):
        print('[Caution] ' + k + ' vanished!')

    for k in set(after_params.keys()) - set(before_params.keys()):
        print('[Info] ' + k + ' is added!')

    for v in before_params.keys():
        before_obj = before_params[v]['params']
        after_obj = after_params[v]['params']
        if before_obj['api_timeout'] == after_obj['api_timeout'] and before_obj['height'] == after_obj['height'] and \
           before_obj['width'] == after_obj['width'] and before_obj['callback'] == after_obj['callback'] and \
           before_obj['creative_options'] == after_obj['creative_options'] and before_obj['js_file'] == after_obj['js_file'] \
                and before_obj['zone_id'] == after_obj['zone_id']:
            print('Product [Criteo] is no problem')
        else:
            if 'api_timeout' not in before_obj.keys():
                print(v + ' api_timeout [key] is not exist\n')
                continue
            if before_obj['callback'] != after_obj['callback']:
                print('Callback in adprodset_code ' + v + ' is different')
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
            if before_obj['creative_options'] != after_obj['creative_options']:
                print('creative_options in adprodset_code ' + v + ' is different')
            else:
                print(v + ' creative_options is OK')
            if before_obj['zone_id'] != after_obj['zone_id']:
                print('zone_id in adprodset_code ' + v + ' is different')
            else:
                print(v + ' zone_id is OK')


