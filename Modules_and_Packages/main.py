# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# importing from a module
from mymodule import my_func
# importing from a Package
from MyMainPackage import some_mainscript
from MyMainPackage.SubPackage import mysubscript

#importing function from a package
from MyMainPackage.some_mainscript import report_main



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    my_func()

    report_main()

    some_mainscript.report_main()
    mysubscript.sub_report()
