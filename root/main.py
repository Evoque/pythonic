import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import StreamingResponse

# from dependencies import get_query_token
# from routers import items, users

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

# app.include_router(users.router)
# app.include_router(items.router)


@app.get("/")
async def root():
    return {"message": "Hello Evoque"}


async def fake_video_streamer():
    for i in range(10):
        yield f"some fake video bytes --{i}".encode("utf-8")


@app.get("/stream")
async def main():
    return StreamingResponse(fake_video_streamer())


"""
is to have some code that is executed when your file is called with `python myapp.py`

"""
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
