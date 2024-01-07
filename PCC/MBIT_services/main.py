from typing import List
from fastapi import FastAPI, HTTPException

from PCC.MBIT_services.database import MBTITestQuestion
from .models import MBTITestResult

app = FastAPI()

# This is a placeholder for MBTI test questions
mbti_test_questions = []

# Route to retrieve MBTI test questions
@app.get("/mbti/questions", response_model=List[MBTITestResult])
async def get_mbti_questions():
    if not mbti_test_questions:
        raise HTTPException(status_code=404, detail="No MBTI test questions available")
    return mbti_test_questions

@app.post("/mbti/submit", response_model=MBTITestResult)

async def submit_mbti_test(result: MBTITestResult):
    # Calculate the MBTI type based on the answers
    calculated_mbti_type = calculate_mbti_type(result.test_questions)
    result.mbti_type = calculated_mbti_type

    # Add the submission to the list of results
    mbti_test_results.append(result)

    return result

def calculate_mbti_type(questions: List[MBTITestQuestion]) -> str:
    # Logic to calculate the MBTI type based on the answers
    # Replace this with your actual calculation

    # For demonstration purposes, we'll assume the user selected the first option for all questions
    answers = [0] * len(questions)
    for i, question in enumerate(questions):
        answers[i] = question.scores[0]

    # Calculate the scores for each dimension (I/E, N/S, etc.)
    dimension_scores = [sum(answers[i::4]) for i in range(4)]

    # Determine the MBTI type based on the scores
    mbti_type = ""
    if dimension_scores[0] >= 2:
        mbti_type += "I"
    else:
        mbti_type += "E"
    if dimension_scores[1] >= 2:
        mbti_type += "N"
    else:
        mbti_type += "S"
    if dimension_scores[2] >= 2:
        mbti_type += "F"
    else:
        mbti_type += "T"
    if dimension_scores[3] >= 2:
        mbti_type += "P"
    else:
        mbti_type += "J"

    return mbti_type
