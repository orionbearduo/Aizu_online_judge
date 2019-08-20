if __name__ == '__main__':
    def dividing_source(file_name):
        all_lines1 = open(file_name).readlines()
        for line in all_lines1:
            data = {}
            m = line.split('')
            if len(m) <= 1:
                continue
            for i in m:
                b = i.split('')
                data[b[0]] = b[1]
        return data['source_id']


    bf_source = dividing_source('/Users/icko/Documents/000/criteo/stg/adprodsetbetabefore891100')
    af_source = dividing_source('/Users/icko/Documents/000/criteo/stg/adprodsetbetaafter891100')
    print(bf_source)
    if bf_source == af_source:
        print("source id is ok")