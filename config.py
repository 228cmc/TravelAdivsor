import os
from dotenv import load_dotenv

load_dotenv()  # Loads the environment variables from the .env file

DATABASE_URI = os.getenv("DATABASE_URI")
