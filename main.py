import imp
from shutil import move
from fastapi import FastAPI

app = FastAPI()

students = [
{
"name": "",
"class": "",
"year": 0
},
{
"name": "Ramu",
"class": "9th",
"year": 1964
},
{
"name": "Maru",
"class": "11th",
"year": 200
},
{
"name": "Jani",
"class": "12th",
"year": 2005
},
{
"name": "Viju",
"class": "10th",
"year": 2013
}

]

# Home Page Message
@app.get("/")
async def root():
    return {'message':'welcome'}

# All Cars
@app.get("/students")
def get_students():
    return students

# Single Car
@app.get("/student/{student_id}")
def get_car(student_id:int):
    return students[student_id-1]

# Delete
@app.delete("/student/{student_id}")
def delete_car(student_id:int):
    students.pop(student_id)
    return {"message":"Movie has been deleted successfully"}

# Adding - POST
@app.post("/create_car")
def create_car(student:dict):
    students.append(student)
    return students[-1]

# Update Car
@app.post("/update_car")
def update_car(student_id:int, student:dict):
    student_updated = students[student_id]
    student_updated['name'] = student['name'] 
    student_updated['class'] = student['class'] 
    student_updated['year'] = student['year']
    students[student_id] = student_updated
    return student_updated

web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}

# pip install fastapi
# pip install "uvicorn[standard]"
# uvicorn main:app --reload