import re

# Precompile regex

pattern = re.compile(r'(Len|Neverm)ore', re.IGNORECASE)

def main():
    with open('raven.txt') as f:
        for line in f:
            # re.sub(r'(Len|Neverm)ore', '###', line):
            match  = re.search(pattern, line)
            if match:
                # print match.group()
                print pattern.sub('###', line)

if __name__ == '__main__':
    main()