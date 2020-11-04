try:
    num_1=int(input("enter a number:"))
    num_2=int(input("enter the number:"))
    num_1/num_2
except ZeroDivisionError as err:

    print("infinity")
except ValueError:
    print("invalid input")
else:
    print(num_1/num_2)
finally:
    print("always excecute this statements")
    print(num_1+num_2)
