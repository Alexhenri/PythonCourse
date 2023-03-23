# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import inspect

def PrintFrame():
  callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  print(info.filename)                      # __FILE__     -> Test.py
  print(info.function)                      # __FUNCTION__ -> Main
  print(info.lineno)                        # __LINE__     -> 13

def fiboask():
    # Use a breakpoint in the code line below to debug your script.
    n = int(input("Choose a number to get the fibo result\n"))
    return n

def wants_continue():
    while True:
        action = input("Do you want to continue?\n")
        if action == "Yes" or action == "Y":
            return True
        else:
            return False

def fibo_func(x):

    check = x in fibo_d
    if check == False:
        result = fibo_func(x-1) + fibo_func(x-2)
        fibo_d[x] = result
    else:
        result = fibo_d[x]
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    fibo_d = {1:1, 2:1}
    loop = True


    while loop:
        x = fiboask()
        print(fibo_func(x))
        #loop = wants_continue()
        if x > 10:
            loop = False

    print(fibo_d)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
