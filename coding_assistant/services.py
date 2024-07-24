from common.prompts import CODING_ASSISTANT_PROMPT
from common.rag import create_rag_chain


rag_chain = create_rag_chain("coding assistant", CODING_ASSISTANT_PROMPT)

def assist_coding_service(game: str, previous_socrates_question: str, student_prompt: str):
    input_context = f"game: {game}\n\nprevious_socrates_question: {previous_socrates_question}\n\nquestion: {student_prompt}"
    return rag_chain.invoke({"input": input_context})