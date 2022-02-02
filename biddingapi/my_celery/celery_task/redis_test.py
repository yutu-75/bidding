import redis


# r = redis.StrictRedis(host='127.0.0.1',password='500237', port=6379, db=2)
r = redis.StrictRedis(host='127.0.0.1',password='123456', port=6379, db=1)
a = r.set('foo', 'bar')
# print(a)
print(r.flushall())


r = redis.StrictRedis(host='127.0.0.1',password='123456', port=6379, db=2)
a = r.set('foo', 'bar')
# print(a)
print(r.flushall())




