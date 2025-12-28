from dotenv import load_dotenv
load_dotenv()


from monitor import monitor
from logger import logger

if __name__ == "__main__":
    monitor(logger)