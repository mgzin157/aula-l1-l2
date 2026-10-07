import random

CARACTERES = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
senha = ""
psw_length = int(input("insira o comprimento da sua senha"))
for i in range (psw_length):
    new_password += random.choice(CARACTERES)
    print ("nova senha gerada" + new_password)
