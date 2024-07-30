from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from coding_assistant.router import router as coding_assistant_router
import uvicorn

app = FastAPI()

origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:3000",  
    "http://localhost:8000", 
    "http://127.0.0.1:8000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(coding_assistant_router, prefix="/api", tags=["assistant"])

#push to vercel
if __name__ == "__main__":
    uvicorn.run(app)

