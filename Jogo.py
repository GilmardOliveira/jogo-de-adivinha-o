import random
import math

# Entrada do intervalo
lower = int(input("Digite o limite inferior: "))
upper = int(input("Digite o limite superior: "))

# Validação do intervalo
if lower >= upper:
    print("Erro: o limite inferior deve ser menor que o limite superior.")
    exit()

# Geração do número secreto
secret_number = random.randint(lower, upper)

# Cálculo do número máximo de tentativas
max_attempts = math.ceil(math.log2(upper - lower + 1))

print(
    f"\nVocê tem {max_attempts} tentativas "
    f"para descobrir o número entre {lower} e {upper}.\n"
)

attempts = 0

while attempts < max_attempts:

    guess = int(input("Adivinhe o número: "))
    attempts += 1

    if guess == secret_number:
        print(
            f"\n🎉 Parabéns! Você acertou em "
            f"{attempts} tentativa(s)."
        )
        break

    elif guess < secret_number:
        print("⬆️ Tente novamente! O número é maior.")

    else:
        print("⬇️ Tente novamente! O número é menor.")

else:
    print(
        f"\n😔 Suas tentativas acabaram."
        f"\nO número era {secret_number}."
        f"\nMais sorte na próxima vez!"
    )
