import asyncio


fpath = 'data/file.dat'


@asyncio.coroutine
def read_line():
    file_content = yield from open(fpath, 'r')

if __name__ == '__main__':
    for line in read_line():
        print(line)
