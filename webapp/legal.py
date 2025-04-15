import os
import signal
import sys
import vertexai
import random
from langchain_google_vertexai import VertexAI, VertexAIEmbeddings,VectorSearchVectorStore
from langchain.chains import RetrievalQA
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage


# Connect to resourse needed from Google Cloud
llm = VertexAI(model_name="gemini-2.0-flash")

