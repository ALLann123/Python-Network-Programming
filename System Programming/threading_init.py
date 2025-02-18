#!/usr/bin/python3
import threading

def myTask(message):
    print("Hello World: {} from {}".format(message, threading.current_thread().name))

# Fix: Add a trailing comma in the args tuple
thread1 = threading.Thread(target=myTask, args=("Hello from thread 1",))  
thread2 = threading.Thread(target=myTask, args=("Hello from thread 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("\nFinished threading!!")
