import redis


# r = redis.StrictRedis(host='47.108.162.205',password='500237', port=6379, db=2)
r = redis.StrictRedis(host='49.4.31.249',password='listendata315*', port=6379, db=1)
a = r.set('foo', 'bar')
# print(a)
print(r.flushall())


r = redis.StrictRedis(host='49.4.31.249',password='listendata315*', port=6379, db=2)
a = r.set('foo', 'bar')
# print(a)
print(r.flushall())




