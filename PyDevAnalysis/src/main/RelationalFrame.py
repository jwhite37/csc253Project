'''
Created on Nov 30, 2014

Creating a graph lab frame as we would expect to see
in a relational database.

Thus - Session Data -> Submission Data

Keys for the frame

Session ID - Unique primary key for each session
IP Address - IP Address where the session originates from
Python Version - either 2 or 3 version of python
Interest - Is this a session of interest to us (0 or 1 flag bit)
Submissions - Dictionary of submissions attributed to this session
    Submission ID - Key for indexing each submission
    Dict - Submission Data
        Date/Time - Date and Time of the submission
        Code Segment - Code submitted by the user for this submission
        Error Message - Compile Error Message for this submission (if any)
        Error Flag - Compile Error Flag (0 or 1) for this submission

THIS STILL HAS SOME WORK NEEDED IT WOULD SEEM...

@author: jeffery
'''

import graphlab as gl
from graphlab import SFrame
from graphlab import SArray

def process_frame(frame_name):
    
    #Setup columns for the new frame
    session_id = []
    ip_address = []
    python_version = []
    interest = []
    submissions = []
    
    #Load in the frame we're processing
    frame = gl.load_sframe(frame_name)
    
    #Sort the frame by IP and then DT ASC
    sorted_frame = frame.sort(['ip','dt'])
    
    #Previous IP to see if we're looking at a new IP address
    previous_ip = 0
    previous_py = 0
    
    #Counters (for keys)
    record_counter = 1
    submission_counter = 1
    
    #Dictionary to hold submissions
    submissions_collection = {}
    
    #Looping through all records to break this up into
    #ip address and then 'session' chunks
    for i in xrange(len(sorted_frame)):
        if(i == 1):
            print sorted_frame['ip'][i]
            break;
        if(i % 100 == 0):
            print "processing record:" + str(i)
        if((sorted_frame['ip'][i] != previous_ip)):
            if(previous_ip != 0):
                #Add in the record to the frame
                session_id += str(record_counter)
                ip_address += str(previous_ip)
                python_version += str(previous_py)
                interest += str(is_interesting(submissions_collection))
                submissions += submissions_collection
                
                #Reset all values
                submissions_collection = {}
                previous_ip = sorted_frame['ip'][i]
                previous_py = sorted_frame['py'][i]
                record_counter = record_counter + 1
                submission_counter = 1
                
                #Create and append the submission
                d = {}
                d['date-time'] = sorted_frame['dt'][i]
                d['code_segment'] = sorted_frame['user_script'][i]
                d['error_message'] = sorted_frame['err_msg'][i]
                d['error_flag'] = sorted_frame['compile_err'][i]
                
                submissions_collection[str(submission_counter)] = d
                submission_counter = submission_counter + 1
                
            else:
                #Handling the very first record
                previous_ip = sorted_frame['ip'][i]
                previous_py = sorted_frame['py'][i]
                
                #Create and append the submission
                d = {}
                d['date-time'] = sorted_frame['dt'][i]
                d['code_segment'] = sorted_frame['user_script'][i]
                d['error_message'] = sorted_frame['err_msg'][i]
                d['error_flag'] = sorted_frame['compile_err'][i]
                
                submissions_collection[str(submission_counter)] = d
                submission_counter = submission_counter + 1
        else:
            #Create and append the submission
            d = {}
            d['date-time'] = sorted_frame['dt'][i]
            d['code_segment'] = sorted_frame['user_script'][i]
            d['error_message'] = sorted_frame['err_msg'][i]
            d['error_flag'] = sorted_frame['compile_err'][i]
            
            submissions_collection[str(submission_counter)] = d
            submission_counter = submission_counter + 1
            
    #Finally, create the frame and save it!
    
    print ip_address
    print len(session_id)
    print len(ip_address)
    print len(python_version)
    print len(submissions)
    
    rst = SFrame()
    rst.add_column(SArray(session_id, dtype=str), name='session_id')
    rst.add_column(SArray(ip_address, dtype=str), name='ip_address')
    rst.add_column(SArray(python_version, dtype=str), name='python_version')
    rst.add_column(SArray(submissions, dtype=dict), name='submissions')

    rst.save("test_frame")          

def is_interesting(user_submissions):
    return 1
    
def main():
    process_frame("py2_error_frame_clean")
    
if __name__ == '__main__':
    main()