# Python Level 1
# Week 9 HW Solutions
# Kavan Lam
# Nov 27, 2021

# Question 1
for row in range(7, 0, -1):
    print("*" * row)

for row in range(2, 8):
    print("*" * row)
    

# Question 2
print("-----------------------------------------------------------")
list_of_num = [9, 8, 90, 51, 60, 83, 2, 25, 73]

new_list = []
for number in list_of_num:
    if number >= 50 and number <= 85:
        new_list.append(number)

print(new_list)


# Question 3
print("-----------------------------------------------------------")
punctuation_and_special = [".", "," , ":", ";", "!", "?", "$", "@", "%", "#"]
my_string = "Hello, My name is $John? and I love CS!!"

new_string = ""
for character in my_string:
    if not character in punctuation_and_special:
        new_string = new_string + character

print(new_string)
