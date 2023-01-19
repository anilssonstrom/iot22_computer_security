from string import digits, ascii_letters, punctuation
from itertools import product


def print_passcodes():
    # V1: 4 siffror
    # for passcode in product(digits, repeat=4):
    #     print(*passcode)

    # V2: 4 bokstäver
    # for passcode in product(ascii_letters, repeat=4):
    #     print(*passcode)

    # V3: 8 bokstäver, siffror, specialtecken
    loops = 0
    for passcode in product(ascii_letters + digits + punctuation, repeat=8):
        print(*passcode)
        loops += 1  # Skriv ut för att se hur många kombinationer som fanns
        
    print("Done!")


if __name__ == '__main__':
    import timeit
    password_time = timeit.timeit(lambda: print_passcodes(), number=1)

    print(f"Time to print all: {password_time:.3} seconds")
