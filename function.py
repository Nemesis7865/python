
# def myFunction(a, b): # prototype
#     print(a + b)

# myFunction(2, 4)


# def suc(a, b):
#     print (a ** b)
# suc(4, 0)

def fizzbuzz():
    for x in range (0, 100):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

fizzbuzz()



