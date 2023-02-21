from itertools import permutations

chars = input('Enter your chars: ')

chars = list(chars)
passwords = permutations(chars)

with open('passwords.txt', 'a') as file:
    for p in passwords:
        c = ''.join(p)
        file.write(c + '\n')
    file.close()
    print('Ok! Password list done.')
