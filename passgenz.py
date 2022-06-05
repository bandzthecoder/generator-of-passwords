import random

print(" ____    ____  ____       ____   ____  _____ ___         _")
print("░██████╗░███████╗███╗░░██╗██████╗░░█████╗░░██████╗░██████╗")
print("██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝")
print("██║░░██╗░█████╗░░██╔██╗██║██████╔╝███████║╚█████╗░╚█████╗░")
print("██║░░╚██╗██╔══╝░░██║╚████║██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗")
print("╚██████╔╝███████╗██║░╚███║██║░░░░░██║░░██║██████╔╝██████╔╝")
print("░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░")
print("----------------------------------------------------------")
print("salut! allons génerer un mot de passe!")

### Define a list of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

### Prompt the user
passwordLength = int(input("quel longueur veut tu que sois ton mot de passe? "))

### Generate a random password
newPassword = []
for x in range(passwordLength):
    ### Append a random character to the password string
    newPassword.append(random.choice(characters))

### Join the whole list back into a string
finalPassword = ''.join(map(str, newPassword))

### Let the user know their new password
print("\n ceci est ton nouveau mot de passe: ", finalPassword)


print("creer par miobandz")
