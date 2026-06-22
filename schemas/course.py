from pydantic import BaseModel


class CourseRequest(BaseModel):
    topic : str
    days : int

class CourseResponse(BaseModel):
    topic : str
    days : int
    roadmap : dict
    resources : list[str]