def pyramid(number):
    levels = number
    for i in range (levels):
        print (str(i) * i)
    return " "

print(pyramid(6))