from src.pipline.training_pipeline import TrainPipeline
from src.logger import configure_logger

configure_logger()
pipline = TrainPipeline()
pipline.run_pipeline()
