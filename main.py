import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("Введите длину пароля "))
result = ""

for i in range(pass_len):
    result += random.choice(chars)

print("ваш пароль:", result)
