import random

# Himani@14
def generate_password(length=10,isspecialcharcater=True,isnumber=True):
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers='1234567890' if isnumber else''
    symbol='!@#$%^&*()_-+{[||(:,.<></)]}'if isspecialcharcater else ''

    all=lowercase+uppercase+numbers+symbol
    
    if length<1:
        raise ValueError("length of pasword alteast  1 ")

    password=''.join(random.choice(all) for i in range(length))
    return password

password=generate_password(length=10,isspecialcharcater=False,isnumber=True)
print(password)