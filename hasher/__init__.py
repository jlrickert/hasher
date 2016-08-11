import hashlib

def hasher(file_name, hash_type='sha1'):
    h = getattr(hashlib, hash_type)()

    with open(file_name, 'rb') as fh:
        chunk = 0
        while chunk != b'':
            chunk = fh.read(1024)
            h.update(chunk)
    return h.hexdigest()
