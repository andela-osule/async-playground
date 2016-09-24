import re

# Search and replace

def main():
    with open('raven.txt') as f:
        for line in f:
            # re.sub(r'(Len|Neverm)ore', '###', line):
            match  = re.search(r'(Len|Neverm)ore', line)
            if match:
                print line.replace(match.group(), '###')

if __name__ == '__main__':
    main()