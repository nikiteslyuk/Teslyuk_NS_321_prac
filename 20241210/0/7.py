import asyncio


async def prod(q):
    for i in range(5):
        st = f"value_{i}"
        await q.put(st)
        print(f"prod: put {st} to q1")
        await asyncio.sleep(1)


async def mid(q1, q2):
    while True:
        res = await q1.get()
        print(f"mid: got {res} from q1")
        await q2.put(res)
        print(f"mid put {res} to q2")


async def cons(q):
    while True:
        res = await q.get()
        print(f"cons: got {res} from q2")
    return


async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    ptask = asyncio.create_task(prod(q1))
    mtask = asyncio.create_task(mid(q1, q2))
    ctask = asyncio.create_task(cons(q2))
    await ptask
    # mtask.cancel()
    # ctask.cancel()


asyncio.run(main())
