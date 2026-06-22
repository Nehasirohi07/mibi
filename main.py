from fastapi import FastAPI

from agents.orchestrator import create_learning_plan

from schemas.course import (
    CourseRequest,
    CourseResponse
)

app = FastAPI()



@app.get("/")
def home():
    return{
        "message":"Mibi Backend Running"
    }

@app.post(
        "/course",
        response_model = CourseResponse
          )
def create_course(course: CourseRequest):
    
    result = create_learning_plan(
        course.topic,
        course.days
    )

    return {
        "topic": course.topic,
        "days":course.days,
        **result 
    }