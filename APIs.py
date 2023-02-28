from main import app
from Connection import cnx
from schemas import TaskUpdate, TaskCreate, UserSchema, UserLoginSchema
from auth import signJWT
from Exceptions import invalid_user
from fastapi import Depends
from protection import authenticate


@app.get("/tasks", tags=["fetch"])
async def get_tasks():
    # To get all tasks
    with cnx.cursor() as cursor:
        cursor.execute("SELECT * FROM Task")
        results = cursor.fetchall()
    return results


# To get a specific task with id: tak_is
@app.get("/tasks/{id}", tags=["fetch"])
async def get_tasks(id: int):
    # To get a specific task
    with cnx.cursor() as cursor:
        cursor.execute("SELECT * FROM Task WHERE id=%s", id)
        results = cursor.fetchone()
    return results


# Define the POST endpoint to create a new task
@app.post("/tasks", tags=["create"], dependencies=[Depends(authenticate)])
async def create_task(task: TaskCreate):
    # Insert the new task into the database
    with cnx.cursor() as cursor:
        sql = "INSERT INTO Task (name, description, status) VALUES (%s, %s, %s)"
        cursor.execute(sql, (task.name, task.description, task.status))
        cnx.commit()

    # Return a success message
    return {"message": "Task created successfully"}


# To update a specific task with id : task_id
@app.put("/tasks/{task_id}", tags=["update"], dependencies=[Depends(authenticate)])
async def update_task(task_id: int, task_update: TaskUpdate):
    # Update the task in the database
    with cnx.cursor() as cursor:
        sql = "UPDATE Task SET name=%s, description=%s, status=%s WHERE id=%s"
        cursor.execute(sql, (task_update.name, task_update.description, task_update.status, task_id))
        cnx.commit()

    # Return a success message
    return {"message": "Task updated successfully"}


# To clear all tasks
@app.delete("/tasks", tags=["delete"], dependencies=[Depends(authenticate)])
async def clear_tasks():
    # Delete all tasks from the database
    with cnx.cursor() as cursor:
        sql = "DELETE FROM Task"
        cursor.execute(sql)
        cnx.commit()

    # Return a success message
    return {"message": "All tasks deleted successfully"}


# To clear a tasks
@app.delete("/tasks/{id}", tags=["delete"], dependencies=[Depends(authenticate)])
async def clear_tasks(id: int):
    # Delete all tasks from the database
    with cnx.cursor() as cursor:
        sql = "DELETE FROM Task WHERE id=%s"
        cursor.execute(sql, id)
        cnx.commit()

    # Return a success message
    return {"message": f"A task with id {id} deleted successfully"}


@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema):
    # Create new user into the database
    with cnx.cursor() as cursor:
        sql = "INSERT INTO User (fullname, email, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user.fullname, user.email, user.password))
        cnx.commit()

    # Return a success message
    return {"Message": f"New user created {user.fullname}"}


@app.post("/user/login", tags=["user"])
def login_user(credential: UserLoginSchema):
    # Login user
    with cnx.cursor() as cursor:
        sql = "SELECT fullname FROM User WHERE email=%s and password=%s"
        cursor.execute(sql, (credential.email, credential.password))
        username = cursor.fetchone()
        if username is None:
            raise invalid_user

    # Return a success message
    return signJWT(credential.email)
