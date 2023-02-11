"""not my code but I wanted to keep it to review and understand as it helped me formulate my answer. Had to google this all() Lots of shortcuts in python and I would much rather know how to "list comprehension" EVERYTHING lol."""

# def are_consecutive_numbers(numbers):
#     return all(numbers[i] == numbers[i - 1] + 1 for i in range(1, len(numbers)))


#So number(i) equal to numbers(i-1) plus 1 
    #for loop i in range of 1 to the length of the list (numbers)
    
    # One other not is I could have tested for duplicates which would have made the answer immediately
    # False if any were found.  
    
    # if (len(a_list)) != len(set(a_list)):  (not my code) set() is an easy way to remove duplicates
    
    # Ex. from w3school.com
x = set(("apple", "banana", "cherry","apple", "banana", "cherry"))

print(x)
#output: {'cherry', 'apple', 'banana'} ***it remove the second "set" with the same names

    