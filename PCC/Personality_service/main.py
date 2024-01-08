from fastapi import FastAPI

app = FastAPI()

# Define the personality data
personality_data = {
    "ISTJ": {
        "Personality Attributes": "Introvert, Sensing, Thinking, Judging",
        "Traits": "Planner who likes to carefully plan their future, organized, focused and likes to pay attention to details, realistic, responsible, and adopts a logical approach to achieve their life goals. Loyal, trustworthy, and dependable. Likes to follow rules and desires to maintain structure.",
        "Suitable Career": "Accountant, Military Leader, Lawyer, Computer Programmer, Librarian, Dentist, Police Officer or Detective, and Doctor",
    },
    "ISFJ": {
        "Personality Attributes": "Introvert, Sensing, Feeling, Judging",
        "Traits": "Introvert, emotional and impassive, focus on concentrate facts, appreciate useful ideas and like things in order. Accountant, Administrator, Bookkeeper, Banker, Child care provider, Nurse, Counselor, Paralegal, Office Manager, Teacher, and Social worker",
        "Suitable Career": "Accountant, Administrator, Bookkeeper, Banker, Child care provider, Nurse, Counselor, Paralegal, Office Manager, Teacher, and Social worker",
    },
    "INFJ": {
        "Personality Attributes": "Introvert, Intuition, Feeling, Judging",
        "Traits": "Compassionate, decisive, doers, empathetic, soft-spoken, organized, and logical who like to sort their matters beforehand. Introvert by nature, have a strong and meaningful bond with people, and like helping people around. Artist, Photographer, Actor, Psychologist, Teacher, Writer, Entrepreneur, Counselor, Religious worker, Librarian, and Musician",
        "Suitable Career": "Artist, Photographer, Actor, Psychologist, Teacher, Writer, Entrepreneur, Counselor, Religious worker, Librarian, and Musician",
    },
    "INTJ": {
        "Personality Attributes": "Introvert, Intuition, Thinking, Judging",
        "Traits": "Prefer working alone, perceive information intuitively, gather logical and objective information, preplan their possessions, like to control their space by themselves, able to understand and evaluate complex information. Architecting, Science, Engineering, Doctor, Dentist, Teacher, Lawyer, and Judge",
        "Suitable Career": "Architecting, Science, Engineering, Doctor, Dentist, Teacher, Lawyer, and Judge",
    },
    "ISTP": {
        "Personality Attributes": "Introvert, Sensing, Thinking, Perceiving",
        "Traits": "Introvert who likes to spend time alone and think about ideas and things, likes new experiences and enjoys hands-on activities, quick in identifying problems and takes serious actions to resolve problems, makes logical decisions, cool-headed, reserved, and good at coping with crises. Perform well in tasks that offer freedom; prefer working on practical and real-world applications. Forensic science, Computer programming, Carpentry, Engineering, Photographer, Physical therapist, Software engineer, Law enforcement, Firefighter, Mechanics, Scientist, and Pilot",
        "Suitable Career": "Forensic science, Computer programming, Carpentry, Engineering, Photographer, Physical therapist, Software engineer, Law enforcement, Firefighter, Mechanics, Scientist, and Pilot",
    },
    "ISFP": {
        "Personality Attributes": "Introvert, Sensing, Feeling, Perceiving",
        "Traits": "Quiet, sensitive, peaceful, considerate, friendly, and appreciative, like to keep their options open and do not rush in driving conclusions, focus on the details, enjoys the moment rather worrying about the future; prefer working on practical applications and acquire hands-on experience. Artist, Veterinarian, Chef, Composer or musician, Pediatrician, Naturalist, Social worker, Designer, Teacher, Forest ranger, Psychologist, and Nurse",
        "Suitable Career": "Artist, Veterinarian, Chef, Composer or musician, Pediatrician, Naturalist, Social worker, Designer, Teacher, Forest ranger, Psychologist, and Nurse",
    },
    "INFP": {
        "Personality Attributes": "Introvert, Intuition, Feeling, Perceiving",
        "Traits": "Reserved, Intuitive who ignores minor details and focuses on the big picture. Values harmony, makes decisions based on their personal values and advocates their personal beliefs. Spiritual and creative, they like to work alone and prefer to express their thoughts by writing rather than speaking. Artist, Social Worker, Writer Counselor, Librarian, Social Worker, Graphic Designer, Writer, Psychologist, and Physical Therapist",
        "Suitable Career": "Artist, Social Worker, Writer Counselor, Librarian, Social Worker, Graphic Designer, Writer, Psychologist, and Physical Therapist",
    },
    "INTP": {
        "Personality Attributes": "Introvert, Intuition, Thinking, Perceiving",
        "Traits": "Calm, reserved, analytical, interested in theoretical concepts, think logically while making decisions, focus on the big picture, keep their options open and limit themselves to plan their forthcomings, drive information logically, creative thinking, believe in personal freedom, and get offended by people who try to suppress their ability to work and think for themselves. Chemist, Physicist, Computer programmer, Forensic scientist, Engineer, Mathematician, Pharmacist, Software developer, and Geologist",
        "Suitable Career": "Chemist, Physicist, Computer programmer, Forensic scientist, Engineer, Mathematician, Pharmacist, Software developer, and Geologist",
    },
    "ESTP": {
        "Personality Attributes": "Extrovert, Sensing, Thinking, Perceiving",
        "Traits": "Impulsive and action-oriented, active in identifying and evaluating problems, makes decisions quickly, prefers straightforward and practical information, good in establishing active relationships with people. Computer support technician, Sales agent, Paramedic, Detectives, Police officer, Entrepreneur, and Marketer",
        "Suitable Career": "Computer support technician, Sales agent, Paramedic, Detectives, Police officer, Entrepreneur, and Marketer",
    },
    "ESFP": {
        "Personality Attributes": "Extrovert, Sensing, Feeling, Perceiving",
        "Traits": "Spontaneous, adventurous, resourceful, and practical, perceptive and understanding who recognizes intentions of actions. Artist, Fashion designer, Actor, Human resources specialist, Counselor, Psychologist, Social worker, Musician, Child care provider, and Athletic coach",
        "Suitable Career": "Artist, Fashion designer, Actor, Human resources specialist, Counselor, Psychologist, Social worker, Musician, Child care provider, and Athletic coach",
    },
    "ENFP": {
        "Personality Attributes": "Extrovert, Intuition, Feeling, Perceiving",
        "Traits": "Extroverts who are genuinely concerned about people around them, creative and charismatic who like new ideas and focus on the outcome rather than the present, flexible and spontaneous who like to keep their options open. Psychologist, Counselor, Politician, Journalist, TV Anchor/Reporter, Actor, Nutritionist, Social Worker, and Nurse",
        "Suitable Career": "Psychologist, Counselor, Politician, Journalist, TV Anchor/Reporter, Actor, Nutritionist, Social Worker, and Nurse",
    },
    "ENTP": {
        "Personality Attributes": "Extrovert, Intuition, Thinking, Perceiving",
        "Traits": "Great communication skills; enjoy interacting and being around people, like engaging people in debates. Prefer to focus on the future rather than the present, intuitively make quick decisions, wait for the situation to unfold by itself, creative and tend to focus on the world around them, quick in imbibing ideas and situations around, like to learn other people’s points of view and help people see the other side of the story. Engineer, Scientist, Journalist, Lawyer, Psychiatrist, Psychologist, and Inventor",
        "Suitable Career": "Engineer, Scientist, Journalist, Lawyer, Psychiatrist, Psychologist, and Inventor",
    },
    "ESTJ": {
        "Personality Attributes": "Extrovert, Sensing, Thinking, Judging",
        "Traits": "Values rules, prefers privacy, and follows traditions; often gets involved in community organizations and government branches. Rigid, stubborn, confident, doer, predictable, hard worker, cooperative, punctual, practical, harsh, and critical. Police officer, Banker, Military, Business manager, Judge, School administrator, Politician, Accountant, and Teacher",
        "Suitable Career": "Police officer, Banker, Military, Business manager, Judge, School administrator, Politician, Accountant, and Teacher",
    },
    "ESFJ": {
        "Personality Attributes": "Extrovert, Sensing, Feeling, Judging",
        "Traits": "Social, organized, loyal, confused, sensitive, scheduled, and generous. They are good at observing people around them and support and help them accordingly. Childcare, Office manager, Social work, Physician, Counseling, Teaching, Receptionist, Bookkeeper, and Nursing",
        "Suitable Career": "Childcare, Office manager, Social work, Physician, Counseling, Teaching, Receptionist, Bookkeeper, and Nursing",
    },
    "ENFJ": {
        "Personality Attributes": "Extrovert, Intuition, Feeling, Judging",
        "Traits": "Extroverts, supportive, and warm, encourage and help people around, resolve disagreements, and ease tensions. Counselor, Psychologist, Social worker, Teacher, Human resources manager, Manager, and Sales representative",
        "Suitable Career": "Counselor, Psychologist, Social worker, Teacher, Human resources manager, Manager, and Sales representative",
    },
    "ENTJ": {
        "Personality Attributes": "Extrovert, Intuition, Thinking, Judging",
        "Traits": "Strong leadership skills, self-assured, well-organized, good at making decisions, assertive, outspoken, and strong communication skills. Impatient, stubborn, insensitive, aggressive, and intolerant",
        "Suitable Career": "Human resources manager, Software developer, University professor, Company CEO or manager, Business analyst, Lawyer, Entrepreneur, and Scientist",
    },
}

@app.get("/get_personality_info/{personality}")
async def get_personality_info(personality: str):
    if personality.upper() in personality_data:
        return personality_data[personality.upper()]
    else:
        return {"error": "Personality type not found."}
