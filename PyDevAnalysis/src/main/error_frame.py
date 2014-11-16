'''
Created on Nov 15, 2014

@author: jeffery

Creating a frame that contains flags for compile errors
in the provided script
'''

from graphlab import SFrame
from graphlab import SArray
import json

def main():
    with open('../../Data/data_file_modified.txt') as data:
        sf = SFrame()
        
        id = []
        dt = []
        ip = []
        py = []
        script = []
        error = []        
        
        for i, line in enumerate(data):
            jo = json.loads(line)
            
            id += [i]
            dt += jo['dt']
            ip += jo['ip']
            py += jo['py']            
            script += jo['user_script']            
            
            flag = False
            try:
                compile(str(jo['user_script']),'<string>','exec')
            except SyntaxError:
                flag = True

            if(flag):
                error += str(0)
            else:
                error += str(1)        

        '''
        print len(id)
        print len(dt)
        print len(ip)
        print len(py)
        print len(script)
        print len(error)
        '''
                
        sf = sf.add_column(SArray(id), name='id')
        sf.add_column(SArray(dt), name='dt')
        sf.add_column(SArray(ip), name='ip')
        sf.add_column(SArray(py, dtype=str), name='py')
        sf.add_column(SArray(script), name='user_script')
        sf.add_column(SArray(error), name='compile_err')

        sf.save('error_frame')



if __name__ == '__main__':
    main()