from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommenderPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline")

            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)

            logger.info("Pipeline Initialized Successfully")

        except Exception as e:
            logger.error(f"Failed to fetch valid recommendation {str(e)}")
            raise CustomException("Error during fetching recommendation", e)
    
    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Recieved a query: {query}")

            recommendation = self.recommender.get_recommendation(query=query)

            logger.info("Recommendation generated successfully")

            return recommendation
        
        except Exception as e:
            logger.error(f"Failed to generate recommendation {str(e)}")
            raise CustomException("Error during generating recommendation", e)