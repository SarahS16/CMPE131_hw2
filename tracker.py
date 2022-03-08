
def func_counter(func):
    def counter():
        counter.has_been_called = True
        return func
    counter.has_been_called = False



        


