
class Bucket:
    def __init__(self, volume, temperature):
        self.volume = volume
        self.temperature = temperature

    def __str__(self):
        return "Bucket with volume {} l and temperature {} C.".format(self.volume, self.temperature)

    def __add__(self, other):
        new_volume = self.volume + other.volume
        new_temperature = (self.volume * self.temperature + other.volume * other.temperature) / new_volume
        return Bucket(new_volume, new_temperature)

    def sub_buckets(self, size):
        volume = self.volume
        while volume > size:
            volume -= size
            yield Bucket(volume=size, temperature=self.temperature)

        if volume > 0:
            yield Bucket(volume=volume, temperature=self.temperature)

    def __iter__(self):
        return self.sub_buckets(size=1)



bucket =  Bucket(volume=7.5, temperature=10)

for sub_bucket in bucket.sub_buckets(size=2):
   print(sub_bucket)

print("aaaaaaaaaaaaaaaa")

for i, sub_bucket in enumerate(bucket):
   print(i, sub_bucket)

