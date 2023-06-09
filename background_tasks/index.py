"""
You can define background tasks to be run after returning a response.

Examples:
1. Email notifications: return the response right away and `send the email notification in the background`
2. Processing data: return a reponse of "Accepted" (received a file) and process it in the background

#TODO 大任务执行 `https://docs.celeryq.dev/en/stable/` & `https://fastapi.tiangolo.com/project-generation/`
"""
from typing import Annotated

from fastapi import BackgroundTasks, FastAPI, Depends
from fastapi.testclient import TestClient

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """
    FastAPI will create the object of type `BackgroundTasks` for you and pass it as that parameter.
    """
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_notification, message)
    return q


@app.post("/send-notification2/{email}")
async def send_notification2(
    email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_notification, message)
    return {"message": "Message send"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
