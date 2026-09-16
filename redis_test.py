import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)



#r.rpush("farmerqueue","FarmerA")

#r.rpush("farmerqueue","FarmerB")

#r.rpush("farmerqueue","FarmerC")

#print(r.lrange("farmerqueue", 0, -1))

#r.lpop("farmerqueue")
#r.lrem("farmerqueue",1,"FarmerB")#r.lrem(key, count, value)

#print(r.lrange("farmerqueue", 0, -1))
#print(r.lrange("farmerqueue", 0, -1))

r.sadd("users","Mubarak")
r.sadd("users","Vivek")

