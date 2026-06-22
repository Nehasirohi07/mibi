from fastapi import FastAPI
from pydantic import BaseModel 
from agents.course_planner import generate_course_plan
from agents.web_search_agent import search_topic
from agents.orchestrator import create_learning_plan

app = FastAPI()

class CourseRequest(BaseModel):
    topic: str
    days: int


@app.get("/")
def home():
    return{
        "message":"Mibi Backend Running"
    }

@app.post("/course")
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