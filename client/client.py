import redis
import time

# 1. Подключение к Redis
r = redis.Redis(host='redis', port=6379, db=0)

# 2. Создание объекта PubSub
pubsub = r.pubsub()

# 3. Подписка на канал
channel_name = 'news_channel'
pubsub.subscribe(channel_name)
for message in pubsub.listen():
    print(message)
