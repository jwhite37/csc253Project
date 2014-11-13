__author__ = 'Qiyuan Qiu, Jeffery White'

from graphlab import SFrame
import json


def main():
    with open('../../Data/data_file_modified.txt') as data:
        sf = SFrame()
        for i, line in enumerate(data):
            new_row = SFrame(json.loads(line))
            sf = sf.append(new_row)
	sf.save('python_tutor')
        sf.show()

if __name__ == '__main__':
    main()
