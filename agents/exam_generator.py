def generate_exam(topic):
    return[
        {
            "question":f"what is {topic}",
            "type":"theory"
        },
        {
            "question":f"Explain important concepts of {topic}",
            "type":"theory"
        },
        {
            "question":f"Build a mini project using {topic}",
            "type":"practical"
        }
    ]