#!/usr/bin/env python2.7
# from: http://lonelycode.com/2011/02/04/python-threading-and-queues-and-why-its-awesome/
import threading
import time

class count_stuff(threading.Thread):
    """
        A thread class that will count a number, sleep and output that number
    """
    def __init__ (self, start_num, end):
        self.num = start_num
        threading.Thread.__init__ (self)
   
    def run(self):
        while True:
            if self.num != end:
                self.num += 1
                print "Outputting: ", str(self.num)
                time.wait(5)
            else:
                break
       
myThread = count_stuff(1, 5)
myThread.start()
