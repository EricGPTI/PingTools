import os

print('#' * 60)
address = input("Digite o IP ou Nome do Host a ser verificado: ")

print('-' * 60)
os.system(f'ping -n 6 {address}')
print('-' * 60)
