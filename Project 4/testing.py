#!/usr/bin/env -S python3 -u


def main():
    number = '0000011'
    print(len(number))
    hi = str(int(number) + 1).zfill(len(number))
    print(hi)
    print(len(hi))

    

if __name__ == "__main__":
    main()