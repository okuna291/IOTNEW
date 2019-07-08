#!/usr/bin/env python
import threading
import time
import logging
import random
import urllib2
import urllib
from threading import Thread

###########################
###The simplest way to use a Thread is to instantiate it with a target function and call start() to let it begin working.

# def worker():
#     print 'Worker'
#     return

# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()

#############

# def get_responses():
#     urls = ['http://www.google.com', 'http://www.amazon.com', 'http://www.ebay.com', 'http://www.alibaba.com', 'http://www.reddit.com']
#     start = time.time()
#     for url in urls:
#         print url
#         resp = urllib2.Request(url)
#         # resp = urllib2.urlopen(resp)
#         # print resp.getcode()
        
#     print "Elapsed time: %s" % (time.time()-start)

# get_responses()


############# MULTI THREADING

# class GetUrlThread(Thread):
#     def __init__(self, url):
#         self.url = url 
#         super(GetUrlThread, self).__init__()

#     def run(self):
#         resp = urllib2.urlopen(self.url)
#         print self.url, resp.getcode()

# def get_responses():
#     urls = ['http://www.google.com', 'http://www.amazon.com', 'http://www.ebay.com', 'http://www.alibaba.com', 'http://www.reddit.com']
#     start = time.time()
#     threads = []
#     for url in urls:
#         t = GetUrlThread(url)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print "Elapsed time: %s" % (time.time()-start)

# get_responses()


###########################

# some_var = 0

# class IncrementThread(Thread):
#     def run(self):
#         #we want to read a global variable
#         #and then increment it
#         global some_var
#         read_value = some_var
#         print "some_var in %s is %d" % (self.name, read_value)
#         some_var = read_value + 1 
#         print "some_var in %s after increment is %d" % (self.name, some_var)

# def use_increment_thread():
#     threads = []
#     for i in range(50):
#         t = IncrementThread()
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print "After 50 modifications, some_var should have become 50"
#     print "After 50 modifications, some_var is %d" % (some_var,)

# use_increment_thread()



###########################
### Pass arguments to thread

# def worker(num):
#     """thread worker function"""
#     print 'Worker: %s' % num
#     return

# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()

###########################
### Naming your thread

# def worker():
#     print threading.currentThread().getName(), 'Starting'
#     time.sleep(2)
#     print threading.currentThread().getName(), 'Exiting'

# def my_service():
#     print threading.currentThread().getName(), 'Starting'
#     time.sleep(3)
#     print threading.currentThread().getName(), 'Exiting'

# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # use default name

# w.start()
# w2.start()
# t.start()

###########################
### Logging threads

# logging.basicConfig(level=logging.DEBUG,
#                     format='[%(levelname)s] (%(threadName)-10s) %(message)s',
#                     )

# def worker():
#     logging.debug('Starting')
#     time.sleep(2)
#     logging.debug('Exiting')

# def my_service():
#     logging.debug('Starting')
#     time.sleep(3)
#     logging.debug('Exiting')

# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # use default name

# w.start()
# w2.start()
# t.start()

###########################
### Thread daemon

# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )

# def daemon():
#     logging.debug('Starting daemon')
#     time.sleep(10)
#     logging.debug('Exiting daemon')

# d = threading.Thread(name='daemon', target=daemon)
# d.setDaemon(True) # set true to turn deamon mode on

# def non_daemon():
#     logging.debug('Starting non daemon')
#     logging.debug('Exiting non daemon')

# t = threading.Thread(name='non-daemon', target=non_daemon)

# d.start()
# t.start()

###########################
### Thread daemon join method

# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )

# def daemon():
#     logging.debug('Starting daemon')
#     time.sleep(10)
#     logging.debug('Exiting daemon')

# d = threading.Thread(name='daemon', target=daemon)
# d.setDaemon(True)

# def non_daemon():
#     logging.debug('Starting non daemon')
#     logging.debug('Exiting non daemon')

# t = threading.Thread(name='non-daemon', target=non_daemon)

# d.start()
# t.start()

# d.join()
# t.join()

###########################
### Thread daemon join method - time out

# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )

# def daemon():
#     logging.debug('Starting daemon')
#     time.sleep(10)
#     logging.debug('Exiting daemon')

# d = threading.Thread(name='daemon', target=daemon)
# d.setDaemon(True)

# def non_daemon():
#     logging.debug('Starting non daemon')
#     logging.debug('Exiting non daemon')

# t = threading.Thread(name='non-daemon', target=non_daemon)

# d.start()
# t.start()

# d.join(5)
# print 'd.isAlive()', d.isAlive()
# t.join()

###########################
### signaling between threads

# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )
                    
# def wait_for_event(e):
#     """Wait for the event to be set before doing anything"""
#     logging.debug('wait_for_event starting')
#     event_is_set = e.wait()
#     logging.debug('event set: %s', event_is_set)

# def wait_for_event_timeout(e, t):
#     """Wait t seconds and then timeout"""
#     while not e.isSet():
#         logging.debug('wait_for_event_timeout starting')
#         event_is_set = e.wait(t)
#         logging.debug('event set: %s', event_is_set)
#         if event_is_set:
#             logging.debug('processing event')
#         else:
#             logging.debug('doing other work')


# e = threading.Event()
# t1 = threading.Thread(name='block', 
#                       target=wait_for_event,
#                       args=(e,))
# t1.start()

# t2 = threading.Thread(name='non-block', 
#                       target=wait_for_event_timeout, 
#                       args=(e, 2))
# t2.start()

# logging.debug('Waiting before calling Event.set()')
# time.sleep(3)
# e.set()
# logging.debug('Event is set')

###########################
### locking threads

# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )
                    
# class Counter(object):
#     def __init__(self, start=0):
#         self.lock = threading.Lock()
#         self.value = start
#     def increment(self):
#         logging.debug('Waiting for lock')
#         self.lock.acquire()
#         try:
#             logging.debug('Acquired lock')
#             self.value = self.value + 1
#         finally:
#             self.lock.release()

# def worker(c):
#     for i in range(2):
#         pause = random.random()
#         logging.debug('Sleeping %0.02f', pause)
#         time.sleep(pause)
#         c.increment()
#     logging.debug('Done')

# counter = Counter()
# for i in range(2):
#     t = threading.Thread(target=worker, args=(counter,))
#     t.start()

# logging.debug('Waiting for worker threads')
# main_thread = threading.currentThread()
# for t in threading.enumerate():
#     if t is not main_thread:
#         t.join()
# logging.debug('Counter: %d', counter.value)
