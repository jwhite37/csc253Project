__author__ = 'Qiyuan Qiu, Jeffery White'

from graphlab import SFrame
import json

n_total_lines = 220000

def main():
    with open('../../Data/data_file_modified.txt') as data:
        sf = SFrame()
        for i, line in enumerate(data):
            new_row = SFrame(json.loads(line))
            sf = sf.append(new_row)
            if i % 10000 == 0:
                print float(i) / n_total_lines
        sf.save('python_tutor')
        sf.show()

if __name__ == '__main__':
    main()
