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
    
    loaded_frame = graphlab.load_sframe("py2_ready_for_session")

    print loaded_frame.column_names()
    #print loaded_frame['user_script'][1]

if __name__ == '__main__':
    main()
