import asyncio
import random


async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    if middle < finish:
        await event_in2.wait()
    i, j, k = start, middle, start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1
    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1
    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1
    event_out.set()


async def mtasks(A):
    ln = len(A)
    A1, A2 = A[:], [0] * ln
    tasks = []
    events = []

    for i in range(ln):
        event = asyncio.Event()
        event.set()
        events.append(event)

    length = 1
    flip = True

    while length < ln:
        new_events = []
        for start in range(0, ln, 2 * length):
            middle = min(start + length, ln)
            finish = min(start + 2 * length, ln)
            event_in1 = events[start // length]
            event_in2 = events[middle // length] if middle < ln else asyncio.Event()
            event_out = asyncio.Event()
            new_events.append(event_out)
            task = merge(
                A1 if flip else A2,
                A2 if flip else A1,
                start,
                middle,
                finish,
                event_in1,
                event_in2,
                event_out,
            )
            tasks.append(task)
        events = new_events
        length *= 2
        flip = not flip

    return tasks, A1


import sys

exec(sys.stdin.read())
