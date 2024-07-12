lista = []
sum = 0

while True:
    num = int(input())
    if num != 55:
        lista.append(num)
        sum += num
    else:
        break
print(len(lista))
print(sum)
print(round(sum/len(lista)))
