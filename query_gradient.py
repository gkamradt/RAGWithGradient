from gradientai import Gradient
from dotenv import load_dotenv
import os

load_dotenv()

gradient = Gradient(
        access_token=os.getenv("GRADIENT_ACCESS_TOKEN"),
        workspace_id=os.getenv("GRADIENT_WORKSPACE_ID")
)

result = gradient.answer(
    question="What is the latest on mistral?",
    source={
        "type": "rag",
        "collectionId" : os.getenv("GRADIENT_RAG_ID")
    }
)['answer']

print (result)