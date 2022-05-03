def ask_for_int():
    while True:
        try:
            result = int(input('Please enter a number: '))
        except:
            print('Whoops! That is not a number')
        else:
            print('Thank you!')
            break
        finally:
            print("That's a finally statement")

if __name__ == '__main__':

    ask_for_int()



