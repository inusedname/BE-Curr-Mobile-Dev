import bcrypt

def hashed(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())