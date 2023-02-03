#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
   print(f"hello {user_name.upper()}!")
   
hello_name("Kevin")

# Question 2 (X)
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns 
# nothing

def first_odds():
    for n in range(1,100):
        if n % 2 == 1:
            print(n)
            
first_odds()


# Question 3 (X)
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
   return max(a_list)
         
a_list = [1,2,3,4,55,66,-777,88,777,-1000]
b_list = [1,2,3,4,55,66,777,88,100,-1000]

print(max_num_in_list(a_list))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
   leap = False
   if year % 4 == 0 and year % 100 != 0:
      leap = True     
   elif  year % 400 == 0:
      leap = True
   return leap

year = 4000
print(is_leap_year(year))
print(type(is_leap_year(year)))
   

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
   sorted_list = sorted(a_list)
   print(sorted_list)
   min_max_list = list(range(min(a_list), max(a_list)+1))
   print(list(min_max_list))   
   if sorted_list == min_max_list:
      print("consecutive")
   else:
      print("non-consecutive")

a_list = [5,6,8,4,9,7]
b_list = [4,3,6]

is_consecutive(a_list)
is_consecutive(b_list)

# print(range(min(b_list)))
# print(range(max(b_list)))
# sorted_list = sorted(b_list)
# min_max_list = range(min(sorted_list), max(sorted_list))
# print(list(min_max_list))
list= [1,2,3,4,5]
