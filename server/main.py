# Importing the required libraries
import fastapi
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import mysql.connector
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Get the db password
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Creating the API app from FastAPI
app = fastapi.FastAPI()

# Adding the CORS middleware to the API app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to connect to the database
def connect_db():
    db = mysql.connector.connect(
        host="45.147.7.81",
        user="croco",
        password=DB_PASSWORD,
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
        tasks = cursor.fetchall()
        # Converting the results into a list
        tasks_list = [task for task in tasks]
        # Returning the results
        return tasks_list
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
        # Getting the ID of the newly created task
        task_id = cursor.lastrowid
        # Returning the ID
        return {"id": task_id}
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