from src.bert.knn_search import KNNSearch
from src.bert.redis_conn import RedisConnection

"""Perform simple KNN search in Redis
"""

retriever = KNNSearch("beauty and the beast", RedisConnection().conn())

results = retriever.top_knn()

print(results)
