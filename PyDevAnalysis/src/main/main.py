__author__ = 'Qiyuan Qiu, Jeffery White'

from graphlab import SFrame
import json


def make_sframe(json_dict):
    for key in json_dict.keys():
        # add '[' and ']' to make dict val a list instead of str
        #which is required by graphlab.SFrame
        json_dict[key] = [json_dict[key]]

    return SFrame(json_dict)


def main():
    with open('../../Data/data_file.txt') as data:
        sf = SFrame()
        for i, line in enumerate(data):
            x = json.loads(line)
            new_row = make_sframe(x)
            sf = sf.append(new_row)
            if (i>50):
                break
        sf.show()

if __name__ == '__main__':
    main()
