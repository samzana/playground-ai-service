from pydantic import BaseModel 
from typing import List


class HelpRequest(BaseModel):
    game: str
    previous_socrates_question: str
    student_prompt: str 
