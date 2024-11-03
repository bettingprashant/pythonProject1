# OrderedDict
# Dictionary that remebers insertion order

from collections import OrderedDict, defaultdict

d = {"address": "KA", "name": "Raj", "age": 78, "id":123}
print(d)

dp = dict()
dp["age"] = 78
dp["address"] = 123
dp["name"] = "Raj"
dp["id"] = 44
print(dp)

od = OrderedDict()
od['banana'] = 2
od['apple'] = 1
od['perar'] = 3
print(od)

dd = defaultdict(int)
print(dd)