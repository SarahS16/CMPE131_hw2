def doubler(funct):
    def wrapper():
        funct()
        funct()
    return wrapper
