import os
from dotenv import load_dotenv
from pathlib import Path
from binance.client import Client

# Force load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


client = Client(API_KEY, API_SECRET)

client.API_URL = "https://testnet.binance.vision/api"