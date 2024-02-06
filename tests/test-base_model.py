#!/usr/bin/python3

import time
__import__( base_model


bm = base_model.BaseModel()
bm.attr1 = 2018
print(bm)
print(bm.to_dict())
time.sleep(10) # delay the execution for 10s
bm.save()
print(bm)
