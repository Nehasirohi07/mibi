from agents.course_planner import generate_course_plan
from agents.web_search_agent import search_topic


def create_learning_plan(topic,days):

    roadmap = generate_course_plan(topic , days)

    resources = search_topic(topic)
    
    return{
        "roadmap":roadmap,
        "resources":resources

    }