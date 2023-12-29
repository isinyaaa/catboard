from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Thread(BaseModel):
    title: str
    body: str
    image: str


threads = []


@app.get("/threads/{thread_id}")
async def read_thread(thread_id: int):
    if thread_id > len(threads):
        return {"error": "thread not found"}
    return threads[thread_id]


@app.get("/threads")
async def read_threads(skip: int = 0, limit: int = 50):
    return threads[skip : skip + limit]


@app.post("/threads")
async def create_thread(thread: Thread):
    threads.append(thread)
    return {"thread_id": len(threads) - 1}


@app.put("/threads/{thread_id}")
async def update_thread(thread_id: int, thread: Thread):
    if thread_id > len(threads):
        return {"error": "thread not found"}
    threads[thread_id] = thread
    return {"success": True}
