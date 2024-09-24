# 1 Write a Python program to print the following string in a specific format
# print("""Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are""")


# 2 Write a Python program to find out what version of Python you are using
# import sys

# print(sys.version)
# print(sys.version_info)


# 3. Write a Python program to display the current date and time.
# import datetime

# print(datetime.datetime.now())


#4. Write a Python program that calculates the area of a circle based on the radius entered by the user
# from math import pi

# radius= float(input("Please enter the radius of circle: "))
# area= pi*radius**2
# print("Area of circle is:", area)


# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# message= last_name+ " " + first_name + " " 
# print("Hi Mr.", message)

#6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# numbers= input("Enter a sequence of comma-separated number: ")
# number= numbers.split(",")
# number1=tuple(number)
# print(number)
# print(number1)


# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# extension= input("Please enter your file name with extension: ")
# file_extension= extension.split(".")
# final= file_extension[1]
# print(final)


# 8. Write a Python program to display the first and last colors from the following list.
# color= input("Enter your fav colors with comma-separated: ")
# color_list= color.split(",")
# first_color=color_list[0]
# last_color=color_list[-1]

# print("fist fav color is:",first_color ," ", "Last fav color is:", last_color)

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = input("Enter date: ")
# date=exam_st_date.replace(",", "/")

# print("The examination will start from :",date)


# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# n=input("Enter value: ")
# n1=int(n+n)
# n2=int(n+n+n)

# print("final valuse is:",int(n)+n1+n2)


#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# print(input.__doc__)


# 12. Write a Python program that prints the calendar for a given month and year.
# import calendar

# m=int(input("Enter month: "))
# y=int(input("Enter year: "))

# print(calendar.month(y,m))


#13. Write a Python program to print the following 'here document'.
# here_document=""""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example"""

# print(here_document)

# 14. Write a Python program to calculate the number of days between two dates.
# from datetime import datetime
# user_input = input("Enter a date in YYYY-MM-DD format: ")
# date_object = datetime.strptime(user_input, "%Y-%m-%d")
# date2=datetime.now()

# et=date2-date_object
# print(et)

# 15. Write a Python program to get the volume of a sphere with radius six.
# from math import pi
# r=float(input("Please enter the radius of sphere: "))
# V=(4/3)*((pi)*r**3)
# print("Your total volume of sphere is: ",(V))


# 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
# number=int(input("Enter int: "))
# value=17-number
# if number>17:
#     print(abs(value)*2)
# else:
#     print(value)
    

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
# number=float(input("Enter any number: "))
# if number >999 and number <= 1999:
#     print("Your enter value is btw 100 of 1000")
# elif number>1999 and number<=2999:
#     print("Your enter value is btw 100 of 2000")
# else:
#     print("Your entered value is not in given range!")

# 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
# number1=int(input("enter First number: "))
# number2=int(input("enter second number: "))
# number3=int(input("enter third number: "))
# sum=number1+number2+number3
# if number1==number2==number3:
#     sum=sum*3
# print(sum)


#19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is"

# massage=input("Enter your message: ")
# if massage.startswith("is"):
#     print(massage)
# else: 
#     print(f'is {massage}')
# //////////////W3 method///////////////////
# # Define a function named "new_string" that takes a string parameter called "text"
# def new_string(text):
#     # Check if the length of the "text" is greater than or equal to 2 and if the first two characters of "text" are "Is"
#     if len(text) >= 2 and text[:2] == "Is":
#         # If the conditions are met, return the original "text" unchanged
#         return text
#     else:
#         # If the conditions are not met, prepend "Is" to the "text" and return the modified string
#         return "Is" + text

# # Call the "new_string" function with the argument "Array" and print the result
# print(new_string("Array"))

# # Call the "new_string" function with the argument "IsEmpty" and print the result
# print(new_string("IsEmpty"))



#20 Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

# number = int(input("enter a value: "))
# string= input("enter string: ")

# print(string*number)
# ///////////////////W3//////////////////
# Define a function named "larger_string" that takes two parameters, "text" and "n"
# def larger_string(text, n):
#     # Initialize an empty string variable named "result"
#     result = ""

#     # Use a for loop to repeat the "text" "n" times and concatenate it to the "result"
#     for i in range(n):
#         result = result + text

#     # Return the final "result" string
#     return result

# # Call the "larger_string" function with the arguments 'abc' and 2, then print the result
# print(larger_string('abc', 2))

# # Call the "larger_string" function with the arguments '.py' and 3, then print the result
# print(larger_string('.py', 3))
# 

# 21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
# def even_odd(number):
#     if number % 2 == 0:
#         print(f"your entered number:{number} is even")
        
#     if number % 2 !=0:
#         print(f"your entered number:{number} is odd")

# number = int(input("Enter any number to check if it is even or odd: "))
# even_odd(number)

# 22. Write a Python program to count the number 4 in a given list.
# def check_4(number_list):
#     count=0
#     for i in number_list:
#         if i == 4:
#             count +=1
#     print(f'your list contain {count} numbers of 4')    
            
# number_list=[2,3,4,6,6,3,4,5,0,4,8,4]
# check_4(number_list)

# 23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
# def get_n_copies_for_string(n, name):
#     if len(name) <2:
#         print(name*n)
#     else:
#         print(name[:2]*n)
        
# n = int(input("Enter the number of copies you require: "))
# name = input("Enter the name: ")
# get_n_copies_for_string(n, name)

# 24. Write a Python program to test whether a passed letter is a vowel or not.
# def test_vowel(letter):
#     if letter == "i" or letter== "o" or letter== "u" or letter== "a" or letter== "e":
#         print(letter ," is a vowel")
#     else:
#         print(letter ,"is not a vowel")
        
# letter= input("Enter a single char to check if it is vowel: ")
# test_vowel(letter)

# 25. Write a Python program that checks whether a specified value is contained within a group of values.
# def test_data(number_list, number):
#     if number in number_list:
#         print(number in number_list)
#     else:
#         print(number in number_list) 

# number= int(input("Enter a number to check if it exisit in our list: "))
# number_list=[1,4, 5, 69, 25, 33]

# test_data(number_list, number)
# ///////W3///////////////////
# Define a function called is_group_member that takes two parameters: group_data (a list) and n (an integer).
# def is_group_member(group_data, n):
#     # Iterate through the elements (values) in the group_data list.
#     for value in group_data:
#         # Check if the current value is equal to the given integer, n.
#         if n == value:
#             return True  # If found, return True.
#     return False  # If the loop completes and no match is found, return False.

# # Call the is_group_member function with two different lists and integers, and print the results.
# print(is_group_member([1, 5, 8, 3], 3))  # Output: True (3 is in the list)
# print(is_group_member([5, 8, 3], -1))    # Output: False (-1 is not in the list)\


# 26. Write a Python program to create a histogram from a given list of integers.
# Define a function called histogram that takes a list of items as a parameter.
# def histogram(items):
#     # Iterate through the items in the list.
#     for n in items:
#         output = ''  # Initialize an empty string called output.
#         times = n     # Set the times variable to the value of n.
        
#         # Use a while loop to append '*' to the output string 'times' number of times.
#         while times > 0:
#             output += '*'
#             times = times - 1  # Decrement the times variable.
        
#         # Print the resulting output string.
#         print(output)

# # Call the histogram function with a list of numbers and print the histogram.
# histogram([2, 3, 6, 5])

# 27. Write a Python program that concatenates all elements in a list into a string and returns it.
# def concatenate_list_data(names):
#     name=""
#     for i in names:
#         name+=str(i)
#     print(name)

# names=["a","h","m","a","r"]
# concatenate_list_data(names)
        
# 28. Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# def even_numbers(numbers):
#     for lst in numbers: 
#         if  lst ==237:
#             break
#         elif lst %2==0:
#             print(lst, "even")
            
        
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# even_numbers(numbers)

# 29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# for i in color_list_1:
#     if i not in color_list_2:
#         print(i)
  
# /////////////////////// W3//////////////////////        
# print(color_list_1.difference(color_list_2))


# 30. Write a Python program that will accept the base and height of a triangle and compute its area.
# def cal_area_triangle(height, base):
#     area=(height*base)/2
#     print(area)

# height= int(input("Enter the height of tri-angle: "))
# base= int(input("Enter the base of tri-angle: "))

# cal_area_triangle(height, base)

# 31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
# a=15
# b=20
# def gcd(a,b):
#     if b > a:
#         remainder = b % a
#         while remainder != 0:
#             result=remainder
#             remainder =a % remainder
#         return result
#     elif a > b: 
#         remainder = a % b
#         while remainder != 0:
#             result=remainder
#             remainder =b % remainder       
#         return result

# print(gcd(a,b))
# # 32. Write a Python program to find the least common multiple (LCM) of two positive integers.
# def lcm(a,b):
#     LCM=(a*b)/gcd(a,b)
#     print(LCM)
    
# lcm(a,b)

# 33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
# int1 = int(input("enter 1st value: "))
# int2 = int(input("enter 2nd value: "))
# int3 = int(input("enter 3rd value: "))
# def sum(a,b,c):
#     if a==b or a==c or b==c:
#         print ("sum of 3 integers is: 0")
#     else:
#         add = a+b+c
#         print("sum of 3 integers is: ", add)
# sum(int1,int2,int3)

# 34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
# int1 = int(input("enter 1st value: "))
# int2 = int(input("enter 2nd value: "))
# def sum_of_two(a,b):
#     sum = a +b
#     if sum > 14 and sum < 21:
#         print(20)
#     else:
#         print(sum)
# sum_of_two(int1,int2)
# 35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
# int1 = int(input("enter 1st value: "))
# int2 = int(input("enter 2nd value: "))

# def ret_true(int1,int2):
#     sum = int1 + int2
#     diff = int1- int2
#     if int1==int2 or sum == 5 or abs(diff) == 5:
#         return True
#     else:
#         return False
    
# print(ret_true(int1,int2))


# 36. Write a Python program to add two objects if both objects are integers.
# a=5
# b=5.5


# if type(a) ==int and type(b) ==int:
#     add = a + b
#     print(add)
# else:
#     print("As both given values are not integer type, So You can't add them only this time. You fuckin _________")


# 37. Write a Python program that displays your name, age, and address on three different lines.

# name="Kashif"
# age=69
# address= "Ahmar ka ghr"

# message=[]
# message.append(name)
# message.append(age)
# message.append(address)

# for index,i in enumerate(message):
#     if index == 0:
#         print("name:",i)
#     if index == 1:
#         print("age:",i)
#     if index == 2:
#         print("address:",i)

