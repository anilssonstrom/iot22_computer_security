import random
import secrets

if __name__ == '__main__':
    print(secrets.randbelow(100))
    print(secrets.randbelow(100))
    print(secrets.randbelow(100))
    print(secrets.randbelow(100))
    print(secrets.randbelow(100))
    print(secrets.randbelow(100))
    print(secrets.randbelow(100))
    print(secrets.token_hex(32))

    random.seed(1957263322)
    print(random.randrange(100))
    print(random.randrange(100))
    print(random.randrange(100))
    print(random.randrange(100))
    print(random.randrange(100))
    print(random.randrange(100))
    print(random.randrange(100))
