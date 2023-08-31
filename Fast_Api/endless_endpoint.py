import asyncio

from fastapi import FastAPI
from concurrent.futures.process import ProcessPoolExecutor

app = FastAPI()
pool = ProcessPoolExecutor(max_workers=10)


# ToDo
@app.get("/block")
async def block():
    async def calc():
        k = 0
        while True:
            k += 1
            if k > 1e9:
                break
        return k
    loop = asyncio.get_event_loop()
    res = loop.run_in_executor(pool, calc)
    return {"message": "done", "res": res}


@app.get("/work")
async def work():
    return {"message": "hI"}