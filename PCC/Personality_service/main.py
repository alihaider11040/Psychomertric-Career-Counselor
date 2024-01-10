from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]  # You can replace "*" with the specific origins you want to allow

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Define the personality data
personality_data = {
    "ISTJ": {
        "Personality Attributes": "Introvert, Sensing, Thinking, Judging",
        "Traits": "Planner who likes to carefully plan their future, organized, focused and likes to pay attention to details, realistic, responsible, and adopts a logical approach to achieve their life goals. Loyal, trustworthy, and dependable. Likes to follow rules and desires to maintain structure.",
        "Suitable Career": "Accountant, Military Leader, Lawyer, Computer Programmer, Librarian, Dentist, Police Officer or Detective, Doctor",
    },
    "ISFJ": {
        "Personality Attributes": "Introvert, Sensing, Feeling, Judging",
        "Traits": "Introvert, emotional and impassive, focus on concentrate facts, appreciate useful ideas and like things in order. Accountant, Administrator, Bookkeeper, Banker, Child care provider, Nurse, Counselor, Paralegal, Office Manager, Teacher, and Social worker",
        "Suitable Career": "Accountant, Administrator, Bookkeeper, Banker, Child care provider, Nurse, Counselor, Paralegal, Office Manager, Teacher, Social worker",
    },
    "INFJ": {
        "Personality Attributes": "Introvert, Intuition, Feeling, Judging",
        "Traits": "Compassionate, decisive, doers, empathetic, soft-spoken, organized, and logical who like to sort their matters beforehand. Introvert by nature, have a strong and meaningful bond with people, and like helping people around. Artist, Photographer, Actor, Psychologist, Teacher, Writer, Entrepreneur, Counselor, Religious worker, Librarian, and Musician",
        "Suitable Career": "Artist, Photographer, Actor, Psychologist, Teacher, Writer, Entrepreneur, Counselor, Religious worker, Librarian, Musician",
    },
    "INTJ": {
        "Personality Attributes": "Introvert, Intuition, Thinking, Judging",
        "Traits": "Prefer working alone, perceive information intuitively, gather logical and objective information, preplan their possessions, like to control their space by themselves, able to understand and evaluate complex information. Architecting, Science, Engineering, Doctor, Dentist, Teacher, Lawyer, Judge",
        "Suitable Career": "Architecting, Science, Engineering, Doctor, Dentist, Teacher, Lawyer, Judge",
    },
    "ISTP": {
        "Personality Attributes": "Introvert, Sensing, Thinking, Perceiving",
        "Traits": "Introvert who likes to spend time alone and think about ideas and things, likes new experiences and enjoys hands-on activities, quick in identifying problems and takes serious actions to resolve problems, makes logical decisions, cool-headed, reserved, and good at coping with crises. Perform well in tasks that offer freedom; prefer working on practical and real-world applications. Forensic science, Computer programming, Carpentry, Engineering, Photographer, Physical therapist, Software engineer, Law enforcement, Firefighter, Mechanics, Scientist, Pilot",
        "Suitable Career": "Forensic science, Computer programming, Carpentry, Engineering, Photographer, Physical therapist, Software engineer, Law enforcement, Firefighter, Mechanics, Scientist, and Pilot",
    },
    "ISFP": {
        "Personality Attributes": "Introvert, Sensing, Feeling, Perceiving",
        "Traits": "Quiet, sensitive, peaceful, considerate, friendly, and appreciative, like to keep their options open and do not rush in driving conclusions, focus on the details, enjoys the moment rather worrying about the future; prefer working on practical applications and acquire hands-on experience. Artist, Veterinarian, Chef, Composer or musician, Pediatrician, Naturalist, Social worker, Designer, Teacher, Forest ranger, Psychologist, Nurse",
        "Suitable Career": "Artist, Veterinarian, Chef, Composer or musician, Pediatrician, Naturalist, Social worker, Designer, Teacher, Forest ranger, Psychologist, and Nurse",
    },
    "INFP": {
        "Personality Attributes": "Introvert, Intuition, Feeling, Perceiving",
        "Traits": "Reserved, Intuitive who ignores minor details and focuses on the big picture. Values harmony, makes decisions based on their personal values and advocates their personal beliefs. Spiritual and creative, they like to work alone and prefer to express their thoughts by writing rather than speaking. Artist, Social Worker, Writer Counselor, Librarian, Social Worker, Graphic Designer, Writer, Psychologist, Physical Therapist",
        "Suitable Career": "Artist, Social Worker, Writer Counselor, Librarian, Social Worker, Graphic Designer, Writer, Psychologist, and Physical Therapist",
    },
    "INTP": {
        "Personality Attributes": "Introvert, Intuition, Thinking, Perceiving",
        "Traits": "Calm, reserved, analytical, interested in theoretical concepts, think logically while making decisions, focus on the big picture, keep their options open and limit themselves to plan their forthcomings, drive information logically, creative thinking, believe in personal freedom, and get offended by people who try to suppress their ability to work and think for themselves. Chemist, Physicist, Computer programmer, Forensic scientist, Engineer, Mathematician, Pharmacist, Software developer, Geologist",
        "Suitable Career": "Chemist, Physicist, Computer programmer, Forensic scientist, Engineer, Mathematician, Pharmacist, Software developer, and Geologist",
    },
    "ESTP": {
        "Personality Attributes": "Extrovert, Sensing, Thinking, Perceiving",
        "Traits": "Impulsive and action-oriented, active in identifying and evaluating problems, makes decisions quickly, prefers straightforward and practical information, good in establishing active relationships with people. Computer support technician, Sales agent, Paramedic, Detectives, Police officer, Entrepreneur, Marketer",
        "Suitable Career": "Computer support technician, Sales agent, Paramedic, Detectives, Police officer, Entrepreneur, and Marketer",
    },
    "ESFP": {
        "Personality Attributes": "Extrovert, Sensing, Feeling, Perceiving",
        "Traits": "Spontaneous, adventurous, resourceful, and practical, perceptive and understanding who recognizes intentions of actions. Artist, Fashion designer, Actor, Human resources specialist, Counselor, Psychologist, Social worker, Musician, Child care provider, Athletic coach",
        "Suitable Career": "Artist, Fashion designer, Actor, Human resources specialist, Counselor, Psychologist, Social worker, Musician, Child care provider, and Athletic coach",
    },
    "ENFP": {
        "Personality Attributes": "Extrovert, Intuition, Feeling, Perceiving",
        "Traits": "Extroverts who are genuinely concerned about people around them, creative and charismatic who like new ideas and focus on the outcome rather than the present, flexible and spontaneous who like to keep their options open. Psychologist, Counselor, Politician, Journalist, TV Anchor/Reporter, Actor, Nutritionist, Social Worker, Nurse",
        "Suitable Career": "Psychologist, Counselor, Politician, Journalist, TV Anchor/Reporter, Actor, Nutritionist, Social Worker, and Nurse",
    },
    "ENTP": {
        "Personality Attributes": "Extrovert, Intuition, Thinking, Perceiving",
        "Traits": "Great communication skills; enjoy interacting and being around people, like engaging people in debates. Prefer to focus on the future rather than the present, intuitively make quick decisions, wait for the situation to unfold by itself, creative and tend to focus on the world around them, quick in imbibing ideas and situations around, like to learn other people’s points of view and help people see the other side of the story. Engineer, Scientist, Journalist, Lawyer, Psychiatrist, Psychologist, Inventor",
        "Suitable Career": "Engineer, Scientist, Journalist, Lawyer, Psychiatrist, Psychologist, and Inventor",
    },
    "ESTJ": {
        "Personality Attributes": "Extrovert, Sensing, Thinking, Judging",
        "Traits": "Values rules, prefers privacy, and follows traditions; often gets involved in community organizations and government branches. Rigid, stubborn, confident, doer, predictable, hard worker, cooperative, punctual, practical, harsh, and critical. Police officer, Banker, Military, Business manager, Judge, School administrator, Politician, Accountant, Teacher",
        "Suitable Career": "Police officer, Banker, Military, Business manager, Judge, School administrator, Politician, Accountant, and Teacher",
    },
    "ESFJ": {
        "Personality Attributes": "Extrovert, Sensing, Feeling, Judging",
        "Traits": "Social, organized, loyal, confused, sensitive, scheduled, and generous. They are good at observing people around them and support and help them accordingly. Childcare, Office manager, Social work, Physician, Counseling, Teaching, Receptionist, Bookkeeper, Nursing",
        "Suitable Career": "Childcare, Office manager, Social work, Physician, Counseling, Teaching, Receptionist, Bookkeeper, and Nursing",
    },
    "ENFJ": {
        "Personality Attributes": "Extrovert, Intuition, Feeling, Judging",
        "Traits": "Extroverts, supportive, and warm, encourage and help people around, resolve disagreements, and ease tensions. Counselor, Psychologist, Social worker, Teacher, Human resources manager, Manager, Sales representative",
        "Suitable Career": "Counselor, Psychologist, Social worker, Teacher, Human resources manager, Manager, and Sales representative",
    },
    "ENTJ": {
        "Personality Attributes": "Extrovert, Intuition, Thinking, Judging",
        "Traits": "Strong leadership skills, self-assured, well-organized, good at making decisions, assertive, outspoken, and strong communication skills. Impatient, stubborn, insensitive, aggressive, intolerant",
        "Suitable Career": "Human resources manager, Software developer, University professor, Company CEO or manager, Business analyst, Lawyer, Entrepreneur, Scientist",
    },
}
# Extracting unique professions and their count
strengths_and_weaknesses = {
    "ISTJ": {
        "Strengths": "Detail-oriented, Realistic, Present-focused, Observant, Logical and practical, Orderly and organized",
        "Weaknesses": "Judgmental, Subjective, Tends to blame others, Insensitive",
    },
    "ISFJ": {
        "Strengths": "Reliable, Practical, Sensitive and Eye for detail",
        "Weaknesses": "Dislikes abstract concepts, Avoids confrontation, Dislikes change and Neglects own needs",
    },
    "INFJ": {
        "Strengths": "Sensitive to the needs of others, Reserved, Highly creative and artistic, Focused on the future, Values close, deep relationships, Enjoys thinking about the meaning of life, Idealistic",
        "Weaknesses": "Can be overly sensitive, Sometimes difficult to get to know, Can have overly high expectations, Stubborn, Dislikes confrontation",
    },
    "INTJ": {
        "Strengths": "Enjoys theoretical and abstract concepts, High expectations, Good at listening, Takes criticism well, Self-confident and hard-working",
        "Weaknesses": "Can be overly analytical and judgmental, Very perfectionistic, Dislikes talking about emotions, Sometimes seems callous or insensitive",
    },
    "ISTP": {
        "Strengths": "Logical, Learns by experience, Action-oriented, Realistic and practical, Enjoys new things, Self-confident and easygoing",
        "Weaknesses": "Difficult to get to know, Insensitive, Grows bored easily, Risk-taker, Does not like commitment",
    },
    "ISFP": {
        "Strengths": "Very aware of their environment, Practical, Enjoys hands-on learning, Loyal to values and beliefs",
        "Weaknesses": "Dislikes abstract, theoretical information, Reserved and quiet, Strong need for personal space, Dislikes arguments and conflict",
    },
    "INFP": {
        "Strengths": "Loyal and devoted, Sensitive to feelings, Caring and interested in others, Works well alone, Value close relationships, Good at seeing 'the big picture'",
        "Weaknesses": "Can be overly idealistic, Tends to take everything personally, Difficult to get to know, Sometimes loses sight of the little things, Overlooks details",
    },
    "INTP": {
        "Strengths": "Logical and objective, Abstract thinker, Independent, Loyal and affectionate with loved ones",
        "Weaknesses": "Difficult to get to know, Can be insensitive, Prone to self-doubt, Struggles to follow rules, Has trouble expressing feelings",
    },
    "ESTP": {
        "Strengths": "Gregarious, funny, and energetic, Influential and persuasive, Action-oriented, Adaptable and resourceful, Observant",
        "Weaknesses": "Impulsive, Competitive, Dramatic at times, Easily bored, Insensitive",
    },
    "ESFP": {
        "Strengths": "Optimistic and gregarious, Enjoys people and socializing, Focused on the present, spontaneous, Practical",
        "Weaknesses": "Dislikes abstract theories, Becomes bored easily, Does not plan ahead, Impulsive",
    },
    "ENFP": {
        "Strengths": "Warm and enthusiastic, Empathetic and caring, Strong people skills, Strong communication skills, Fun and spontaneous, Highly Creative",
        "Weaknesses": "Needs approval from others, Disorganized, Tends to get stressed out easily, Can be overly emotional, Overthinks, Struggles to follow rules",
    },
    "ENTP": {
        "Strengths": "Innovative, Creative, Great conversationalist, Enjoys debating, Values knowledge",
        "Weaknesses": "Can be argumentative, Dislikes routines and schedules, Does not like to be controlled, Unfocused, Insensitive",
    },
    "ESTJ": {
        "Strengths": "Practical and realistic, Dependable, Self-confident, Hard-working, Traditional, Strong leadership skills",
        "Weaknesses": "Insensitive, Inflexible, Not good at expressing feelings, Argumentative, Bossy",
    },
    "ESFJ": {
        "Strengths": "Kind and loyal, Outgoing, Organized, Practical and dependable, Enjoy helping others, Conscientious",
        "Weaknesses": "Needy, Approval-seeking, Sensitive to criticism, Dislike change, Intolerant, Controlling",
    },
    "ENFJ": {
        "Strengths": "Outgoing and warm-hearted, Empathetic, Wide social circle, Encouraging, Organized, Affectionate, Persuasive",
        "Weaknesses": "Approval-seeking, Overly sensitive, Indecisive, Self-sacrificing, Rigid and uncompromising, Overprotective, Manipulative",
    },
    "ENTJ": {
        "Strengths": "Strong leadership skills, Self-assured, Well-organized, Good at making decisions, Assertive and outspoken, Strong communication skills",
        "Weaknesses": "Impatient, Stubborn, Insensitive, Aggressive, Intolerant",
    },
}



merged_data = {}

for personality_type, details in personality_data.items():
    strengths = weaknesses = ""
    
    # Retrieve strengths and weaknesses if available
    if personality_type in strengths_and_weaknesses:
        strengths = strengths_and_weaknesses[personality_type]["Strengths"]
        weaknesses = strengths_and_weaknesses[personality_type]["Weaknesses"]

    merged_data[personality_type] = {
        "PersonalityAttributes": details["Personality Attributes"],
        "Traits": details["Traits"],
        "Career": details["Suitable Career"],
        "Strengths": strengths,
        "Weaknesses": weaknesses,
    }


unique_professions = {}
for personality_type, entry in personality_data.items():
    careers = [career.strip() for career in entry.get("Suitable Career", "").split(",")]
    for career in careers:
        if career not in unique_professions:
            unique_professions[career] = 1
        else:
            unique_professions[career] += 1

print(unique_professions)
# Order professions by count in ascending order for a given personality type
def order_professions_by_count(personality_type):
    if personality_type.upper() in personality_data:
        careers = [career.strip() for career in personality_data[personality_type.upper()].get("Suitable Career", "").split(",")]
        sorted_careers = sorted(careers, key=lambda x: unique_professions[x])
        return sorted_careers
    else:
        return []
# FastAPI endpoint to get information based on personality type
@app.get("/get_personality_info/{personality}")
async def get_personality_info(personality: str):
    ordered_professions = order_professions_by_count(personality)
    
    if personality.upper() in merged_data:
        return {"personality_info": merged_data[personality.upper()], "ordered_professions": ordered_professions}
    else:
        return {"error": "Personality type not found."}

