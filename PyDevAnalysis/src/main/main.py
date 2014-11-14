__author__ = 'Qiyuan Qiu, Jeffery White'

from graphlab import SFrame
from graphlab import SArray
import json

n_total_lines = 220000

def main():
    with open('../../Data/data_file_modified.txt') as data:
        sf = SFrame()
        dt = []
        ip = []
        py = []
        script = []
        id = []
        for i, line in enumerate(data):
            jo = json.loads(line)
            dt += jo['dt']
            ip += jo['ip']
            py += jo['py']
            id += [i]
            script += jo['user_script']

            if i % 100 == 0:
                print float(i) / n_total_lines

        sf = sf.add_column(SArray(id), name='id')
        sf.add_column(SArray(dt), name='dt')
        sf.add_column(SArray(ip), name='ip')
        sf.add_column(SArray(py, dtype=str), name='py')
        sf.add_column(SArray(script), name='user_script')

        sf.save('python_tutor')
        sf.show()

if __name__ == '__main__':
    main()
