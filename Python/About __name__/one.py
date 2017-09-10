# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("__name__ is: ",__name__)
    print("one.py is being run directly")
else:
    print("__name__ in one.py is: ",__name__)
    print("one.py is being imported into another module")
