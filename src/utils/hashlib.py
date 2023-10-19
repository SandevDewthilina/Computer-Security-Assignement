import hashlib


def encode(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def verify(raw, encrypted):
    return hashlib.md5(raw.encode('utf-8')).hexdigest() == encrypted
