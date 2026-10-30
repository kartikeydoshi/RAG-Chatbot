from langchain_openai import OpenAIEmbeddings

import os

from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(
    model="jina-embeddings-v5-omni-small",
    api_key=os.getenv("JINA_API_KEY"),
    base_url="https://api.jina.ai/v1",
    check_embedding_ctx_length=False
)

result = embeddings.embed_query("What is artificial intelligence?")
print(len(result))