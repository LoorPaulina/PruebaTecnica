import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_port = os.getenv('DB_PORT', 3306)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    