from gradientai import Gradient
from dotenv import load_dotenv
import os

load_dotenv()

gradient = Gradient(
        access_token=os.getenv("GRADIENT_ACCESS_TOKEN"),
        workspace_id=os.getenv("GRADIENT_WORKSPACE_ID")
    )

rag_collection = gradient.create_rag_collection(
  name="RAG with AI News RSS V3",
  slug="bge-large",
  filepaths=[
    "data/ai_news_rss.txt",
  ],
)

print (f"Your rag_collection.id_ is {rag_collection.id_}")

# 54a5f7d3-c27f-4350-bc68-f23231b6c5f9_rag_config

# # Add more files to your collection if you would like
# rag_id = "your_rag_collection_id"
# rag_collection = gradient.get_rag_collection(id_=rag_id)

# rag_collection.add_files(filepaths = ["docs/one.txt", "docs/two.txt"])