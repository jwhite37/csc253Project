'''
Created on Nov 15, 2014

@author: jeffery

Creating a frame that contains flags for compile errors
in the provided script, as well as the actual error 
produced by the compile function
'''

from graphlab import SFrame
from graphlab import SArray
import json
import re

def main():
    with open('../../Data/data_file_modified.txt') as data:
        sf = SFrame()
        
        # Data model format
        # RecordID | Date/Time | IP Address | Python Version |
        # User Script | Compile Flag | Compile Message
        id = []
        dt = []
        ip = []
        py = []
        script = []
        error = []       
        error_msg = [] 
        
        for i, line in enumerate(data):
            jo = json.loads(line)
            
            # Two different version of Python script
            # need to be compiled on different interpreters
            if(jo['py'][0] == 3):
            
                # Setup the data model we're using
                id += [i]
                dt += jo['dt']
                ip += jo['ip']
                py += jo['py']            
                script += jo['user_script']  
                
                # Run the script on the compile method
                # and obtain any error message
                flag = False
                msg = ""
                
                pattern = "is local and global"
                
                try:
                    compile(jo['user_script'][0],'<string>','exec')
                except SyntaxError, e:
                    if(re.search(pattern, str(e))):
                        msg = "Variable is Local and Global"
                    else:
                        msg = str(e)
                    flag = True
                
                
                if(flag):
                    error += [1]
                else:
                    error += [0] 
                
                # We need to chop off the error type
                # and remove the (filename line number)
                # to have any meaning here.
                fix_msg = msg.partition('(')[0]
                error_msg += [fix_msg.strip()]        
       
        sf = sf.add_column(SArray(id), name='id')
        sf.add_column(SArray(dt), name='dt')
        sf.add_column(SArray(ip), name='ip')
        sf.add_column(SArray(py, dtype=str), name='py')
        sf.add_column(SArray(script), name='user_script')
        sf.add_column(SArray(error), name='compile_err')
        sf.add_column(SArray(error_msg), name='err_msg')

        sf.save('py3_error_frame_clean')




if __name__ == '__main__':
    main()