from fastapi import APIRouter, HTTPException 
from coding_assistant.schemas import HelpRequest
from coding_assistant.services import assist_coding_service


router = APIRouter()

@router.post("/assist")
async def assist_coding(request: HelpRequest):
    try:
        response = assist_coding_service(
            game=request.game,
            previous_socrates_question=request.previous_socrates_question,
            student_prompt=request.student_prompt
        )
        return response["answer"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
