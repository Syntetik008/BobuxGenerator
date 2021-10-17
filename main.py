#imports
import random
import sys

loopnum = 0

many = input("How many to generate: ")  # asks for how many codes to generate

f= open("output.txt","w+")  # creating output.txt

while loopnum < int(many):  # loop
    result_str = ''.join((random.choice('1234567890') for i in range(3)))  # generate code 1
    result_str2 = ''.join((random.choice('1234567890') for i in range(3)))  # generate code 2
    result_str3 = ''.join((random.choice('1234567890') for i in range(3)))  # generate code 3
    result_str4 = ''.join((random.choice('1234567890') for i in range(3)))  # generate code 4
    print(result_str + " " + result_str2 + " " + result_str3 + " " + result_str4)  # show codes
    f.write(result_str + " " + result_str2 + " " + result_str3 + " " + result_str4 + "\n")  # adding codes to output.txt
    loopnum += 1    # add 1 to loop number

input("ok? (press any button)") # closing window
