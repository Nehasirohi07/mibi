from agents.course_planner import generate_course_plan
from agents.web_search_agent import search_topic
from agents.exam_generator import generate_exam

def create_learning_plan(topic,days):

    roadmap = generate_course_plan(topic , days)

    resources = search_topic(topic)

    exam = generate_exam(topic)
    
    return{
        "roadmap":roadmap,
        "resources":resources,
        "exam": exam
    }