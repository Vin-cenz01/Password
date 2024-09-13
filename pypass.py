import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#selection of random  letter
password_list=[]
for i in range(nr_letters):
    r = random.randint(0,25)
    password_list.append(letters[r])
    
#selection of random number

for i in range(nr_numbers):
    r =  random.randint(0,9)
    password_list.append(numbers[r])
    
#selection of random symbol

for i in range(nr_symbols):
    r = random.randint(0,8)
    password_list.append(symbols[r])
    
#thhis is where magic happens
password=""
random.shuffle(password_list)
len_of_pass = nr_letters + nr_numbers + nr_symbols
for i in range(0,len_of_pass):
    password+=password_list[i]
    
print(f"Your generated  Password is {password}")
