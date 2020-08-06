def announce(f):
    def wrapper():
        print("about to run function")
        f()
        print("done with the function")
    return wrapper

@announce
def hello():
    print("hello word")

hello()
