import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")
##LLAMAGUARD_API_KEY = os.getenv("LLAMAGUARD_API_KEY")

FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"