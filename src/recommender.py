from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt
class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()

        self.doc_chain = create_stuff_documents_chain(
            llm = self.llm,
            prompt = self.prompt,
        )

        self.qa_chain = create_retrieval_chain(
            retriever = retriever,
            combine_docs_chain = self.doc_chain,
        )
    
    def get_recommendation(self, query:str):
        result = self.qa_chain.invoke({"input": query})
        print("result", result)
        return result["answer"]
