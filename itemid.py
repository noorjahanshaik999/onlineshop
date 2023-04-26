import random
def itemidotp():
    u_c=[chr(i)for i in range(ord('A'),ord('Z')+1)]
    l_c=[chr(i)for i in range(ord('a'),ord('z')+1)]
    idotp=''
    for i in range(3):
        idotp+=random.choice(u_c)
        idotp+=str(random.randint(0,9))
        idotp+=random.choice(l_c)
    return idotp
