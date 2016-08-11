import hashlib
import sys

from . import hasher


hash_types = [
    'md5',
    'sha1',
    'sha224',
    'sha256',
    'sha384',
    'sha512',
    
]

def main():
    file_names = sys.argv[1:]
    for file_name in file_names:
        d = dict()
        for hash_type in [h.lower() for h in hashlib.algorithms_available]:
            try:
                d[hash_type] = hasher(file_name, hash_type)
            except AttributeError:
                pass
        print(file_name, ':')
        for key in sorted(d.keys()):
            print('\t{} {}'.format(key, d[key]))
        print()


if __name__ == '__main__':
    sys.exit(main())
