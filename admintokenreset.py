from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def admintoken(email,seconds):
    s=Serializer('hfbfe78hjefk',seconds)
    return s.dumps({'admin':email}).decode('utf-8')
