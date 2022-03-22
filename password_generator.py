import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
numbers = '0123456789'
symbol = '[]{}()*&@_'
all = lower+upper+numbers+symbol
my_password_length = 16
my_password = "".join(random.sample(all, my_password_length))
print(my_password)
if my_password[0] in symbol:
  my_password = "".join(random.sample(all, my_password_length))
print(my_password)