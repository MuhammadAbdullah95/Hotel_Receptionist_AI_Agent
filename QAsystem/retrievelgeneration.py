from haystack.utils import Secret
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.retrievers.pinecone import (
    PineconeEmbeddingRetriever,
)
from haystack_integrations.components.generators.google_ai import GoogleAIGeminiGenerator
from haystack import Pipeline
import os
from dotenv import load_dotenv
from QAsystem.utils import pinecone_config
prompt_template = """Answer the following query based on the provided context output should be structured and organized and first refine the output then display it return only the lines of required answer. If the context does
                     not include an answer, reply with 'I don't know'.\n
                     Query: {{query}}
                     Documents:
                     {% for doc in documents %}
                        {{ doc.content }}
                     {% endfor %}
                     Answer: 
                  """


load_dotenv()
gemini_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = gemini_key

def get_result(query: str):
    query_pipeline = Pipeline()

    query_pipeline.add_component("text_embedder", SentenceTransformersTextEmbedder())
    query_pipeline.add_component("retriever", PineconeEmbeddingRetriever(document_store=pinecone_config()))
    query_pipeline.add_component("prompt_builder", PromptBuilder(template=prompt_template))
    query_pipeline.add_component("llm",GoogleAIGeminiGenerator(model="gemini-2.0-flash"))

    query_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
    query_pipeline.connect("retriever.documents", "prompt_builder.documents")
    query_pipeline.connect("prompt_builder", "llm")

    query = query

    results = query_pipeline.run(
        {
            "text_embedder": {"text": query},
            "prompt_builder": {"query": query},
        }
    )

    return results['llm']['replies'][0]

if __name__ == "__main__":
    #loading the environment variable
    '''load_dotenv()
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    
    print("Import Successfully")'''
    
    result=get_result("What are the Factors of Critical Evaluation?")
    print(result)