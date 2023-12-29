from collections import UserList

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Thread(BaseModel):
    title: str
    body: str
    image: str
    _deleted: bool = False


class Threads(UserList[Thread]):
    def exists(self, i) -> bool:
        if i > len(self.data):
            return False
        if self.data[i]._deleted:
            return False
        return True

    def pop(self, i=-1) -> Thread:
        self.data[i]._deleted = True
        return self[i]


threads = Threads()


@app.get("/threads/{thread_id}")
async def read_thread(thread_id: int):
    if threads.exists(thread_id):
        return threads[thread_id]
    return {"error": "thread not found"}


@app.get("/threads")
async def read_threads(skip: int = 0, limit: int = 50):
    return list(filter(lambda t: not t._deleted, threads))[skip : skip + limit]


@app.post("/threads")
async def create_thread(thread: Thread):
    threads.append(thread)
    return {"thread_id": len(threads) - 1}


@app.put("/threads/{thread_id}")
async def update_thread(thread_id: int, thread: Thread):
    if threads.exists(thread_id):
        threads[thread_id] = thread
        return {"success": True}
    return {"error": "thread not found"}


@app.delete("/threads/{thread_id}")
async def delete_thread(thread_id: int):
    if threads.exists(thread_id):
        threads.pop(thread_id)
        return {"success": True}
    return {"error": "thread not found"}
