'''
Created on Nov 15, 2014

@author: jeffery

Simple script to load up a frame we have stored and show it
in the GraphLab web view.

Note: This doesn't actually work from within PyDev, but does
work from my terminal window, probably config stuff
'''

import graphlab

def main():
    
    loaded_frame = graphlab.load_sframe("py2_session_clean")

    check = [25]
    
    test = loaded_frame.filter_by(check, 'session_id')
    
    for e in test:
        print e
    
    

if __name__ == '__main__':
    main()
