#!/usr/bin/env python3

from urllib.parse import urlparse 

#file examples

def main():
    file = "xmp/mtrics"
    print(f"read file w/ urls:")
    with open(file) as file_:
        numb = 0
        for line in file_:
            url = urlparse(line)
            hostname = url.hostname
            path = url.path
            print(f"in any case, need to see h as {hostname} & path as {path}")
            if hostname is not None:
                # if there is None or not BUT not check for validating the returned variable is host has a correct value
                print(f"{numb} - {line.strip()}: where hostname is {hostname} & path is {path}")
            else:
                print(f"not valid url {line}")
            numb += 1

if __name__ == '__main__':
    main()
    exit()
