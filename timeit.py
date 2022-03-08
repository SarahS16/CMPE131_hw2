import time

def calculate_time(funct):
    def wrapper():
        start_t = time.time()
        funct()
        end_t = time.time()
        run_t = end_t - start_t
        print("Total time", run_t)
    return wrapper
    #calculates time of function