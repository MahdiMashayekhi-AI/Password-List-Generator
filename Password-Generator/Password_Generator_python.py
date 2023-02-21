import string
import random

length = int(input('Enter the length of the password: '))

favcar = ')#@%*)($%#)'
text = string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase + favcar

password = ''.join([random.choice(text) for c in range(length)])
print(password)