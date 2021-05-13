import multiprocessing
from config import *
from withdraw import *
from deposit import *
import time

if __name__ == "__main__":
    print("Starting main program")

    # You can try to terminate a process before it is complete
    #time.sleep(.1)
    #stop_withdraw()

    # After 1 second all processes are done
    time.sleep(1)
    
    # With no race condition, this should print 100
    print("Final balance = {}".format(balance.value))
