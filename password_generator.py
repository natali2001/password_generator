import random
import string


lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all,14))

print("Your password:" + password)
