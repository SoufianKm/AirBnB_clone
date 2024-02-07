#!/usr/bin/python3

import time
import base_model


bm = base_model.BaseModel()
bm.attr1 = 2018
print(bm)
print(bm.to_dict())
time.sleep(2)  # delay the execution for 10s
bm.save()
print(bm)

dic = {
        'id': '9d91df14-2e69-46c8-aa07-69d3bda95b55',
        'created_at': '2024-02-06T18:48:35.337483',
        'updated_at': '2024-02-06T18:48:35.337488',
        'attr1': 2018,
        '__class__': 'BaseModel'}

bm2 = base_model.BaseModel(**dic)
print("bm2: \n", bm2)
