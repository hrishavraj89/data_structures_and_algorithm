#Write a python script to calculate the average of elements of a list.
list = [12, 14, 16, 18, 20]

if len(list) == 0:
    print('The list is empty')
else:
    print(f"The average is {sum(list) / len(list)}")