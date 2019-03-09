from random import randrange

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
upper = alphabet.upper()
signs = ",.;_%&*"
all = alphabet+numbers+upper+signs

def gen_passw(all):
    lenght = randrange(5, 25)
    list = []
    for i in range(lenght):
        i = randrange(0,len(all))
        list.append(all[i])
    psw = "".join(list)
    return psw

print(gen_passw(all))
