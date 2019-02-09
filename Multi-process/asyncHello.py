import threading
import asyncio

# without async and await


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 这里是 asyncio 的 sleep 原因是因为这个 sleep 也是一个 coroutine, 所以线程不会等待，而是直接终端去执行下一个任务
    r = yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

# with async and await


async def fuck():
    print(f"fuck world,{threading.currentThread()}")
    r = await asyncio.sleep(1)
    print(f"fuck world again! {threading.currentThread()}")

loop = asyncio.get_event_loop()
tasks = [hello(), hello(), fuck(), fuck()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
