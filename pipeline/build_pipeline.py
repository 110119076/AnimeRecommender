from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from utils.logger import get_logger
from utils.custom_exception import CustomException

from dotenv import load_dotenv
load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Pipeline Build Starting...")
        
        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_info.csv")

        updated_csv = loader.load_and_update()

        logger.info("Data loaded and processed")

        vector_builder = VectorStoreBuilder(updated_csv)
        vector_builder.build_and_store()

        logger.info("Vectorstore built successfully")

        logger.info("Pipeline built successfully")

    except Exception as e:
        logger.error(f"Failed to execute pipeline {str(e)}")
        raise CustomException("Error during pipeline", e)
    

    if __name__ == "__main__":
        main()