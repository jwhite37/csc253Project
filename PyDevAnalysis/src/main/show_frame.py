'''
Created on Nov 15, 2014

@author: jeffery

Simple script to load up a frame we have stored and show it
in the GraphLab web view.

Note: This doesn't actually work from within PyDev, but does
work from my terminal window, proabably config stuff
'''

import graphlab

def main():
    
    loaded_frame = graphlab.load_sframe("python_tutor")

    loaded_frame.show(view='Table')

if __name__ == '__main__':
    main()
