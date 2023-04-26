from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(email,seconds):
    s=Serializer('hfbfe78hjefk',seconds)
    return s.dumps({'user':email}).decode('utf-8')
