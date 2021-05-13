import multiprocessing
from config import *

# function to deposit to account
def deposit(balance, lock):    
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def start_deposit():
    p2.start()

def stop_deposit():
    p2.terminate()

# This start 10 processes when this module is imported
for i in range(10):
    p2 = multiprocessing.Process(target=deposit, args=(balance,lock))
    start_deposit()
    print("Final balance p2 index=" + str(i) + " value=" + str(balance.value))