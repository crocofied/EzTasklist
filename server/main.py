import fastapi
import uvicorn
import mysql.connector
from pydantic import BaseModel

app = fastapi.FastAPI()

def connect_db():
    db = mysql.connector.connect(
        host="45.147.7.81",
        user="croco",
        password="amesadssadsD8.",
        database="ez_tasklist"
    )
    cursor = db.cursor()
    return db, cursor

class Task(BaseModel):
    task: str

@app.get("/tasks/")
def read_root():
    try:
        db, cursor = connect_db()
        cursor.execute("SELECT * FROM tasks")
        tables = cursor.fetchall()
        return {"tasks": tables}
    except:
        raise fastapi.HTTPException(status_code=400, detail="ERROR")

@app.post("/tasks/create/")
def create_task(task: Task):
    try:
        db, cursor = connect_db()
        print(task.task)
        cursor.execute(f"INSERT INTO tasks (task) VALUES ('{task.task}')")
        db.commit()
        return {"status:": "success"}
    except:
        raise fastapi.HTTPException(status_code=400, detail="ERROR")
    
@app.delete("/tasks/delete/")
def delete_task(task_id: int):
    try:
        db, cursor = connect_db()
        cursor.execute(f"DELETE FROM tasks WHERE id = {task_id}")
        db.commit()
        return {"status:": "success"}
    except:
        raise fastapi.HTTPException(status_code=400, detail="ERROR")

uvicorn.run(app, host="localhost", port=8001)