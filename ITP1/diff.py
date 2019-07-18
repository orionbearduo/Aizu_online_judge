import pandas as pd


if __name__ == '__main__':

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
            if len(data) != 0 and data['adprod_type'] == '6':

                subdata = data['adprod_params']
                c = subdata.split('')
                params = {}
                for j in c:
                    d = j.split('')
                    params[d[0]] = d[1]
                result[adprodset_code.strip('\n')] = {'params': params}
        return result

    before_params = dividing('/Users/icko/Documents/000/diff_718/adprodsetbetabefore7181000')
    after_params = dividing('/Users/icko/Documents/000/diff_718/adprodsetbetaafter718940')

    for k in set(before_params.keys()) - set(after_params.keys()):
        print('[Caution] ' + k + ' vanished!')

    for k in set(after_params.keys()) - set(before_params.keys()):
        print('[Info] ' + k + ' is added!')

    for v in before_params.keys():
        before_obj = before_params[v]['params']
        after_obj = after_params[v]['params']
        
        if before_obj['html'] != after_obj['html']:
            print('Html in adprodset_code ' + v + ' is different')
        else:
            print(v + ' Html is OK')
        print(after_obj['width'])

        if 'width' not in before_obj.keys():
            print(v + ' width [key] is not exist')
            continue
        if before_obj['width'] != after_obj['width']:
            print('Width in adprodset_code ' + v + ' is different')
        else:
            print(v + 'Width is OK')

        if 'height' not in before_obj.keys():
            print(v + ' height [key] is not exist')
            continue
        if before_obj['height'] != after_obj['height']:
            print('Width in adprodset_code ' + v + ' is different')
        else:
            print(v + 'Height is OK')



'''
    if before_params == after_params:
        print("OK!")
    else:
        print("There is different")
'''
       # if before_obj['width'] != after_ojb['width']:
        #    print('Width in adprodset_code' + v + 'is different')
       # if before_obj['html'] != after_ojb['html']:
        #    print('Html in adprodset_code' + v + 'is different')
        #if before_obj['html']


    #for v in before_params.values()
        
            

    #def compare(before_params, after_params):
     #   for k in before_params:





    #before_params = dividing('/Users/icko/Documents/000/adprodset.txt')
    #print(before_params)
#    print("----------*****------------")
    #after_params = dividing('/Users/icko/Documents/000/adprodset1.txt')
    #print(after_params)

#    print("********8--------********")



