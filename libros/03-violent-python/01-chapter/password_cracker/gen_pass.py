import hashlib

def gen_hash_512(password):
    return hashlib.sha512(password.encode()).hexdigest()

print(gen_hash_512("hello"))