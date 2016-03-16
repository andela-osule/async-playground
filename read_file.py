import asyncio


fpath = 'data/file.dat'


async def get_file():
    return open(fpath, 'r')

async def read_line():
    f = await get_file()
    for line in f:
        print(line)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(read_line())
    loop.close()
