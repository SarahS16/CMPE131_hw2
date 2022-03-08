from sqlalchemy import false, true


def func_counter(func):
    def counter():
        counter.has_been_called = true
        return func
    counter.has_been_called = false



        


