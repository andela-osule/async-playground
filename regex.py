import re

def main():
    with open('raven.txt') as f:
        for line in f:
            if re.search(r'(Len|Neverm)ore', line):
                print line

if __name__ == '__main__':
    main()