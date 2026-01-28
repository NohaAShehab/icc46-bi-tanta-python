# print("---------------Welcome to inputs module ------------------------")
coursename='python'
def ask_for_number(message='Please enter number') :
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("---- invalid input")
# print(ask_for_number())
def ask_for_string(message='Please enter string') :
    while True:
        mystring = input(message)
        if mystring.isalpha():
            return mystring
        print("---- invalid input")

# some actions needed to run only ?? in the current file
if __name__ == "__main__": #  the entry point of the execution is the current file
    ask_for_number()
    ask_for_string()
    print("Welcome to inputs module")