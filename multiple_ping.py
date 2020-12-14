import os
import time

with open('D:\hosts.txt', 'r') as hosts:
    dump = hosts.read().splitlines()

    for h in dump:
        print(f'Verificando o Host: {h}')
        time.sleep(5)
        print('-' * 60)
        os.system(f'ping -n 2 {h}')
        print('-' * 60)
