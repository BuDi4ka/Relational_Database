import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_HOST', 'db'),  # Use 'localhost' if running outside Docker
            port=os.getenv('POSTGRES_PORT', '5432')
        )
        print("Connection to database established successfully!")
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

