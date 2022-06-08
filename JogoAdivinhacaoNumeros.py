import random
import math

lower = int(input("Entrar com um numero inferior:- "))

upper = int(input("Entrar com um numero superior:- "))

x = random.randint(lower, upper)
print("\n\tVoce só tem ", round(math.log(upper - lower + 1, 2)),"chances para adivnhar o número inteiro\n")

count = 1
while count < math.log(upper - lower +1, 2):
    count += 1
    guess = int(input("Adivinhe o número:- "))

    if x == guess:
        print("\n######## Parabéns você acertou com", count-1, "tentativas o número é: ", x, "########\n")
        break
    elif x > guess:
        print("O Número muito pequeno!")
    elif x < guess:
        print("O Número muito alto!")

    if count >= math.log(upper - lower + 1, 2):
        print("\n###############     O número era:- %d      ################"%x)
        print("############### Mais sorte da proxima vez! ###################\n")