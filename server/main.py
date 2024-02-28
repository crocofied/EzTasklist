# Importing the required libraries
import fastapi
import uvicorn
import mysql.connector
from pydantic import BaseModel

# Creating the API app from FastAPI
app = fastapi.FastAPI()

# Function to connect to the database
def connect_db():
    db = mysql.connector.connect(
        host="45.147.7.81",
        user="croco",
        password="amesadssadsD8.",
        database="ez_tasklist"
    )
    cursor = db.cursor()
    return db, cursor

# Creating a class for the task
class Task(BaseModel):
    task: str

# ----------------- API Endpoints ----------------- #
    
# Endpoint to get all the tasks
@app.get("/tasks/")
def read_root():
    try:
        # Connecting to the database
        db, cursor = connect_db()
        # Get all the tasks from the database
        cursor.execute("SELECT * FROM tasks")
        # Fetching the results
        tables = cursor.fetchall()
        # Returning the results
        return {"tasks": tables}
    except:
        # If there is an error, return an error message
        raise fastapi.HTTPException(status_code=400, detail="ERROR")

# Endpoint to create a new task
@app.post("/tasks/create/")
def create_task(task: Task):
    try:
        # Connecting to the database
        db, cursor = connect_db()
        # Inserting the new task into the database
        cursor.execute(f"INSERT INTO tasks (task) VALUES ('{task.task}')")
        # Committing the changes
        db.commit()
        # Returning the success message
        return {"status:": "success"}
    except:
        # If there is an error, return an error message
        raise fastapi.HTTPException(status_code=400, detail="ERROR")

# Endpoint to delete a task
@app.delete("/tasks/delete/")
def delete_task(task_id: int):
    try:
        # Connecting to the database
        db, cursor = connect_db()
        # Deleting the task from the database
        cursor.execute(f"DELETE FROM tasks WHERE id = {task_id}")
        # Committing the changes
        db.commit()
        # Returning the success message
        return {"status:": "success"}
    except:
        # If there is an error, return an error message
        raise fastapi.HTTPException(status_code=400, detail="ERROR")

# Running the API app
if __name__ == "__main__": 
    # uvicorn.run(app, host="0.0.0.0", port=8001) # For running on a server
    uvicorn.run(app, host="localhost", port=8001) # For running locally