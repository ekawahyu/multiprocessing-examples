import multiprocessing

# creating a lock object and multiprocessing variable
lock = multiprocessing.Lock()
balance = multiprocessing.Value('i', 100)

print("This is configuration module")