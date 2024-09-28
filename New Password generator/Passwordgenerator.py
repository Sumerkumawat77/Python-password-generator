import random 
print("Project : Create A Password Gnerator ! \n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Symbols = ['!', ',', '#', '$', '%', '&', '@', '*', '+']


nr_letters = int(input("How Many letters Would you like in your Password ? \n"))
nr_Symbols = int(input("How Many Symbols Would you like ? \n"))
nr_numbers = int(input("How Many  Numbers would you  like ? \n"))

Password = " "

for char in range(1, nr_letters + 1):
   Password += random.choice(letters)

for char in range(1, nr_numbers + 1):
   Password += random.choice(Numbers)

for char in range(1, nr_Symbols + 1):
   Password += random.choice(Symbols)

print(Password)