import multiprocessing
from config import *

# function to withdraw from account
def withdraw(balance, lock):    
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

def start_withdraw():
    p1.start()

def stop_withdraw():
    p1.terminate()

# This start 10 processes when this module is imported
for i in range(10):
    p1 = multiprocessing.Process(target=withdraw, args=(balance,lock))
    start_withdraw()
    print("Final balance p1 index=" + str(i) + " value=" + str(balance.value))