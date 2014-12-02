'''
Created on Dec 1, 2014

@author: jeffery
'''
import graphlab as gl
from graphlab import SFrame
from graphlab import SArray
from datetime import datetime
import time

def process_frame(filename):
    
    session_id = []
    
    sf = gl.load_sframe(filename)
    
    #Sort the frame by IP and then DT ASC
    sorted_frame = sf.sort(['ip','dt'])
    
    #Variables to keep track of the last record scanned
    #we'll check against these to see if we've moved to
    #a new session or not!
    previous_ip = 0
    previous_dt = ""
    
    #which session are we on currently?
    session_ctr = 0
    
    for e in sorted_frame:
        if(previous_ip != e['ip'] or time_difference(previous_dt,e['dt'])):
            session_ctr = session_ctr + 1
        
        session_id += [session_ctr]
        previous_ip = e['ip']
        previous_dt = e['dt']
    
      
    print len(session_id)
    print len(sf['ip'])
    print session_ctr
    
    sa = gl.SArray(session_id)
    sorted_frame.add_column(sa, name='session_id')
    sorted_frame.save("py3_session_clean")
        
#Return true if the time difference is greater or equal to
#30 minutes!     
def time_difference(start,end):
    fmt = '%Y-%m-%d %H:%M:%S'
    
    #Convert to date time objects
    start_dt = datetime.strptime(start,fmt)
    end_dt = datetime.strptime(end,fmt)
    
    #Convert to Unix time stamps
    start_timestamp = time.mktime(start_dt.timetuple())
    end_timestamp = time.mktime(end_dt.timetuple())
    
    #Calculate the difference in minutes
    difference = (end_timestamp - start_timestamp) / 60
    
    if(difference >= 30):
        return True
    else:
        return False
        
def main():
    process_frame("py3_error_frame_clean")
    
if __name__ == '__main__':
    main()