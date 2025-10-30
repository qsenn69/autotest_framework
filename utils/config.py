import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.aviasales.ru/")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
    ELEMENT_SEARCH_TIMEOUT_S = int(os.getenv("ELEMENT_SEARCH_TIMEOUT_S", "10"))