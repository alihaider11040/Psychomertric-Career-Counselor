from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
import re

app = FastAPI()
origins = ["*"]  # You can replace "*" with the specific origins you want to allow
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


DATABASE_URL = "sqlite:///./test_results.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

results = Table(
    "results",
    metadata,
    Column("id", String, primary_key=True, index=True),
    Column("personality", String),
)

metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# This is a placeholder for MBTI test questions
questions = """
1. You regularly make new friends.
2. You spend a lot of your free time exploring various random topics that pique your interest.
3. Seeing other people cry can easily make you feel like you want to cry too.
4. You often make a backup plan for a backup plan.
5. You usually stay calm, even under a lot of pressure.
6. At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.
7. You prefer to completely finish one project before starting another.
8. You are very sentimental.
9. You like to use organizing tools like schedules and lists.
10. Even a small mistake can cause you to doubt your overall abilities and knowledge.
11. You feel comfortable just walking up to someone you find interesting and striking up a conversation.
12. You are not too interested in discussing various interpretations and analyses of creative works.
13. You are more inclined to follow your head than your heart.
14. You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.
15. You rarely worry about whether you make a good impression on people you meet.
16. You enjoy participating in group activities.
17. You like books and movies that make you come up with your own interpretation of the ending.
18. Your happiness comes more from helping others accomplish things than your own accomplishments.
19. You are interested in so many things that you find it difficult to choose what to try next.
20. You are prone to worrying that things will take a turn for the worse.
21. You avoid leadership roles in group settings.
22. You are definitely not an artistic type of person.
23. You think the world would be a better place if people relied more on rationality and less on their feelings.
24. You prefer to do your chores before allowing yourself to relax.
25. You enjoy watching people argue.
26. You tend to avoid drawing attention to yourself.
27. Your mood can change very quickly.
28. You lose patience with people who are not as efficient as you.
29. You often end up doing things at the last possible moment.
30. You have always been fascinated by the question of what, if anything, happens after death.
31. You usually prefer to be around others rather than on your own.
32. You become bored or lose interest when the discussion gets highly theoretical.
33. You find it easy to empathize with a person whose experiences are very different from yours.
34. You usually postpone finalizing decisions for as long as possible.
35. You rarely second-guess the choices that you have made.
36. After a long and exhausting week, a lively social event is just what you need.
37. You enjoy going to art museums.
38. You often have a hard time understanding other people’s feelings.
39. You like to have a to-do list for each day.
40. You rarely feel insecure.
41. You avoid making phone calls.
42. You often spend a lot of time trying to understand views that are very different from your own.
43. In your social circle, you are often the one who contacts your friends and initiates activities.
44. If your plans are interrupted, your top priority is to get back on track as soon as possible.
45. You are still bothered by mistakes that you made a long time ago.
46. You rarely contemplate the reasons for human existence or the meaning of life.
47. Your emotions control you more than you control them.
48. You take great care not to make people look bad, even when it is completely their fault.
49. Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.
50. When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.
51. You would love a job that requires you to work alone most of the time.
52. You believe that pondering abstract philosophical questions is a waste of time.
53. You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.
54. You know at first glance how someone is feeling.
55. You often feel overwhelmed.
56. You complete things methodically without skipping over any steps.
57. You are very intrigued by things labeled as controversial.
58. You would pass along a good opportunity if you thought someone else needed it more.
59. You struggle with deadlines.
60. You feel confident that things will work out for you.
"""
personality_descriptions = {
    "INTP": "The Logician - Innovative, logical, and reserved. INTPs are known for their curiosity and love of exploring ideas. They enjoy solving complex problems and value intellectual independence.",
    
    "INTJ": "The Architect - Strategic, independent, and analytical. INTJs are natural leaders with a vision for the future. They excel in planning and setting long-term goals, often pursuing them with determination.",
    
    "INFP": "The Mediator - Idealistic, creative, and compassionate. INFPs are driven by their values and seek authenticity in all aspects of life. They are deeply in tune with their emotions and the emotions of others.",
    
    "INFJ": "The Advocate - Insightful, empathetic, and visionary. INFJs are dedicated to making a positive impact on the world. They are often seen as mentors, working towards a better future for others.",
    
    "ISTP": "The Virtuoso - Adventurous, practical, and hands-on. ISTPs excel in using tools and troubleshooting. They are action-oriented, often enjoying the thrill of solving real-world problems.",
    
    "ISTJ": "The Inspector - Responsible, organized, and detail-oriented. ISTJs are known for their practicality and reliability. They thrive in structured environments and are diligent in their work.",
    
    "ISFP": "The Adventurer - Artistic, flexible, and spontaneous. ISFPs value personal expression and enjoy exploring new possibilities. They are often drawn to creative and sensory experiences.",
    
    "ISFJ": "The Defender - Caring, dependable, and nurturing. ISFJs are devoted to supporting others and creating a stable environment. They excel in roles that require empathy and attention to detail.",
    
    "ENTP": "The Debater - Energetic, resourceful, and curious. ENTPs enjoy challenging the status quo and are quick thinkers. They thrive on brainstorming and exploring new ideas.",
    
    "ENTJ": "The Commander - Assertive, strategic, and goal-oriented. ENTJs are natural leaders who enjoy taking charge. They are decisive and work towards achieving their objectives with efficiency.",
    
    "ENFP": "The Campaigner - Enthusiastic, creative, and sociable. ENFPs are passionate about possibilities and connecting with others. They inspire and motivate through their energy and charisma.",
    
    "ENFJ": "The Protagonist - Charismatic, empathetic, and inspiring. ENFJs are natural leaders who care deeply about others. They work towards positive change and are skilled at connecting with people.",
    
    "ESTP": "The Dynamo - Bold, practical, and action-oriented. ESTPs thrive in dynamic and competitive environments. They are often drawn to careers that require quick decision-making.",
    
    "ESTJ": "The Executive - Efficient, organized, and decisive. ESTJs value structure and clear goals. They are dependable leaders who excel in roles that require responsibility and order.",
    
    "ESFP": "The Entertainer - Spontaneous, sociable, and lively. ESFPs enjoy being the center of attention and thrive in social settings. They bring energy and fun to various situations.",
    
    "ESFJ": "The Consul - Supportive, sociable, and responsible. ESFJs are dedicated to maintaining social harmony and helping others. They are often seen as reliable and caring individuals."
}


def extract_questions(questions_string: str) -> List[str]:
    questions_list = questions_string.strip().split("\n")
    return [question[3:].strip() for question in questions_list]

@app.get("/mbit/questions")
async def get_questions():
    return extract_questions(questions)

@app.put("/mbit/edit_questions")
async def edit_questions(updated_questions: str):
    global questions
    questions = updated_questions
    return {"message": "Questions updated successfully"}
def is_valid_answers(answers: Dict[str, int]) -> bool:
    return len(answers) == 60 and all(isinstance(val, int) for val in answers.values())

@app.post("/mbti/submit")
async def submit_answers(email: str, answers: Dict[str, str]):
    if len(answers) != 60:
        raise HTTPException(status_code=400, detail="Invalid number of answers. Expected 60.")

    # Convert string values to integers
    answers = {int(key): int(value) for key, value in answers.items()}

    # Divide answers into 4 sets
    sets = [list(answers.values())[i-1:i+14] for i in range(1, 61, 15)]

    # Calculate personality type
    personality = ""
    for i, answer_set in enumerate(sets, 1):
        if sum(answer_set) < 52:
            personality += "I" if i == 1 else "N" if i == 2 else "F" if i == 3 else "P"
        else:
            personality += "E" if i == 1 else "S" if i == 2 else "T" if i == 3 else "J"

    # Save personality in the database
    db = SessionLocal()
    db.execute(results.insert().values(id=email, personality=personality))
    db.commit()
    db.close()

    return {"personality": personality}

@app.get("/get_description/{personality_type}")
async def get_description(personality_type: str):
    personality_type = personality_type.upper()

    if personality_type not in personality_descriptions:
        raise HTTPException(status_code=404, detail="Personality type not found")

    description = personality_descriptions[personality_type]
    return {"personality_type": personality_type, "description": description}
