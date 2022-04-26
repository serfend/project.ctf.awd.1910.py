import base64
import json
import zlib

with open('configuration.json',encoding='utf-8') as f:
  c = json.load(f)
  c = base64.b85encode(json.dumps(c).encode('utf-8'))
  data = zlib.compress(c)
  data_c = base64.b85encode(data)
  print(data_c)