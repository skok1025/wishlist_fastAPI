from fastapi import FastAPI, HTTPException
from redis import Redis
from pydantic import BaseModel
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

app = FastAPI()
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

class WishItem(BaseModel):
    id: int = None
    task: str
    done: bool


class WishItemCreate(BaseModel):
    task: str
    done: bool


@app.get("/wishlist/")
async def get_wishlist():
    wishlist = redis.zrange("wishlist", 0, -1, withscores=True)
    parsed_wishlist = []
    for item, score in wishlist:
        id, task, done = item.decode().split("||")
        parsed_wishlist.append({
            "id": int(id),
            "task": task,
            "done": done == "T",
            "time": datetime.fromtimestamp(score).strftime('%Y%m%d%H%M%S')
        })
    return parsed_wishlist


@app.post("/wishlist/")
async def add_to_wishlist(item: WishItemCreate):
    score = datetime.now().timestamp()
    id = redis.incr("wishlist_id")
    redis.zadd("wishlist", {f"{id}||{item.task}||{'T' if item.done else 'F'}": score})
    return {"message": "Task added successfully!", "id": id}


@app.delete("/wishlist/{id}")
async def remove_from_wishlist(id: int):
    task_keys = redis.zrangebylex("wishlist", f"[{id}||", f"[{id}||\xff")
    if task_keys:
        redis.zrem("wishlist", *task_keys)
        return {"message": "Task removed successfully!"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
