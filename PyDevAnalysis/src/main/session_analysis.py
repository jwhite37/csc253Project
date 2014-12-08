'''
Created on Dec 7, 2014

@author: jeffery
'''
import graphlab as gl
from graphlab import SFrame
from graphlab import SArray
from datetime import datetime
import time

def process_frame(filename):
    sf = gl.load_sframe(filename)
    
    output_frame = SFrame()
    
    #Setup our output frame
    id = []
    ip = []
    sub_count = []
    error_count = []
    time_count = []
    error_sequence_raw = []
    error_sequence = []
    
    #How many session ID's do we have?
    sa = gl.SArray()
    sa = sf['session_id']
    test = sa.unique()
    
    limit = len(test)
    
    #Start grabbing each session
    for i in range(1,limit):
        
        #Test output
        if (i % 100 == 0):   
            break 
        
        #Get the session and sort it by the date time
        session_frame = sf.filter_by(i,"session_id")
        #sorted_session = session_frame.sort("dt")
        
        row = sf[0]
        
        id += [i]
        ip += [row['ip']]
        sub_count += [len(row)]
        #time_count += [fn_time_count(sorted_session)]
        #error_count += [fn_error_count(sorted_session)]
        #error_sequence_raw += [fn_error_sequence_raw(sorted_session)]
    
    print len(id)
    print len(ip)
    print len(sub_count)
    #print len(time_count)
    
    output_frame = output_frame.add_column(SArray(id), name='id')
    output_frame.add_column(SArray(ip), name='ip')
    output_frame.add_column(SArray(sub_count),name='sub_count')
    #output_frame.add_column(SArray(time_count),name='sub_length')
    #output_frame.add_column(SArray(error_count),name='error_count')
    #output_frame.add_column(SArray(error_sequence_raw,dtype=str),name='err_seq_raw')

    output_frame.save('py2_session_analysis')
        
def fn_time_count(frame):
    sf = SFrame()
    sf = frame
    
    sa = SArray()
    sa = sf['dt']
    
    num = sf.num_rows()
    
    fmt = '%Y-%m-%d %H:%M:%S'
    
    #Convert to date time objects
    start_dt = datetime.strptime(sa[0],fmt)
    end_dt = datetime.strptime(sa[num - 1],fmt)
    
    #Convert to Unix time stamps
    start_timestamp = time.mktime(start_dt.timetuple())
    end_timestamp = time.mktime(end_dt.timetuple())
    
    #Calculate the difference in minutes
    difference = (end_timestamp - start_timestamp) / 60
    
    return difference

def fn_error_count(frame):
    sf = SFrame()
    sf = frame
    
    counter = 0
    
    for e in frame:
        if (e['compile_err'] == 1):
            counter = counter + 1
    
    return counter

def fn_error_sequence_raw(frame):
    sf = SFrame()
    sf = frame
    
    error_string = ""
    
    for e in frame:
        error_string = error_string + " " + e['err_msg']
        
    return error_string

def error_sequence(frame):
    print "Not Implemented"
    
def main():
    process_frame("py2_session_clean")
    
if __name__ == '__main__':
    main()