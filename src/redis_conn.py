from redis_om import get_redis_connection, HashModel, JsonModel, Migrator, EmbeddedJsonModel, Field
import redis
from dotenv import load_dotenv
import os


load_dotenv()

REDIS_CACHE_HOST = os.getenv("REDIS_CACHE_HOST")
REDIS_CACHE_PORT = int(os.getenv("REDIS_CACHE_PORT"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

reDB = redis.StrictRedis(host=REDIS_CACHE_HOST, port=REDIS_CACHE_PORT, db = 0, decode_responses=True, password=REDIS_PASSWORD)