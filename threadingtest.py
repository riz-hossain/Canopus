'''
Created on Feb 12, 2013

@author: Riz
'''

from threading import Timer
import threading
import time

def kill_function():
    print "being called by kill function"
    list_of_thread = threading.enumerate()
    print threading.enumerate()
    for each_thread in list_of_thread:
        print each_thread.name
        if "MainThread" not in each_thread.name:
            print "cancelling an orphan thread"
            print each_thread
    

def another(x):
    #print "i am another funciton"
    #print x
    while 1:
        #print "now i am stuck in another function"
        time.sleep(1)
        if x ==1:
            break
        #print x
    
    
t = Timer(5, kill_function)

x = 1
y = 0
t.start()
print "number of active thread %s" %threading.activeCount()

while x==x:
    print "looping"
    time.sleep(1)
    y =y +1
    print "Thread status: %s" %t.is_alive()
    
    print another(2)
    if y == 6:
        print "cancelling thread"
        t.cancel()
        break
        



#class MC(type):
#  def __repr__(self):
#    return 'Wahaha!'
#
#class C(object):
#  __metaclass__ = MC
#
#print type(C)