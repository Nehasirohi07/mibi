from pydantic import BaseModel

class ExamQuestion(BaseModel):
    question: str
    type: str


class CourseRequest(BaseModel):
    topic : str
    days : int

class CourseResponse(BaseModel):
    topic : str
    days : int
    roadmap : dict
    resources : list[str]
    exam: list[ExamQuestion]

class Resource(BaseModel):
    title:str
    url:str