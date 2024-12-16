import asyncio
from asyncio import Queue

stop_event = asyncio.Event()


async def writer(queue, delay):
    counter = 0
    while not stop_event.is_set():
        await asyncio.sleep(delay)
        await queue.put(f"{counter}_{delay}")
        counter += 1


async def stacker(queue, stack):
    while not stop_event.is_set():
        item = await queue.get()
        await stack.put(item)


async def reader(stack, count, delay):
    for i in range(count):
        await asyncio.sleep(delay)
        item = await stack.get()
        print(item)
    stop_event.set()


async def run(queue, stack, delay1, delay2, delay3, count):
    rdr = asyncio.create_task(reader(stack, count, delay3))
    wtr1 = asyncio.create_task(writer(queue, delay1))
    wtr2 = asyncio.create_task(writer(queue, delay2))
    stckr = asyncio.create_task(stacker(queue, stack))
    await wtr1
    await wtr2
    await stckr
    await rdr


delays = input().strip().split(",")
delay1, delay2, delay3, count = map(int, delays)
stack = Queue()
queue = Queue()

asyncio.run(run(queue, stack, delay1, delay2, delay3, count))
