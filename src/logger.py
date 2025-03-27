# src/logger.py
import logging
import os

def setup_logging():
    # Ensure the logs directory exists
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename='logs/provisioning.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

logger = setup_logging()