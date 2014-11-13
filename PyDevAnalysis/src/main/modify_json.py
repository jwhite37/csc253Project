__author__ = 'qiuqiyuan'

import json

def add_brackets(json_dict):
    for key in json_dict.keys():
        # add '[' and ']' to make dict val a list instead of str
        #which is required by graphlab.SFrame
        json_dict[key] = [json_dict[key]]

    return json_dict

def main():
    with open('../../Data/data_file.txt','r') as data:
        with open('../../Data/data_file_modified.txt', 'w') as out_file:
            for line in data:
                line = add_brackets(json.loads(line))
                out_file.write(json.dumps(line)+'\n')


if __name__ == '__main__':
    main()
