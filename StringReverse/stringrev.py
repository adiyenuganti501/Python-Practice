# name="Adinarayana"
# reverse_name= name[::-1]
# print("The reverse of the name is:", reverse_name)

# nums = [1, 2, 3, 4, 5]
# print(nums[::-2])  # Output: [5, 4, 3, 2, 1]


val=input("Enter a string to reverse: ")
rev_val= val[::-1]
if val ==rev_val:
    print("The string is a palindrome.",rev_val)
else:
    print("The string is not a palindrome.",rev_val)