import random
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', "8","9"]
symbol = ['!', '@','#','$','%','^','&','*','(',')','<','>','?','/']
print("Welcome to Password Generator!")
n_alphabet = int(input("How many letters you want in your password?\n"))
n_symbol = int(input("How many symbols you want in your password\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
password= ""
for i in range(1,n_alphabet+1): 
    char = random.choice(alphabet)
    password += char
for i in range(1,n_symbol+1): 
    char = random.choice(symbol)
    password += char
for i in range(1,n_numbers+1): 
    char = random.choice(numbers)
    password += char
print(password)