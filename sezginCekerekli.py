import json
dosya = open("sezginCekerekli.json", "r")
json_dosya= json.load(dosya)
print("kimlik : " ,json_dosya["kimlik"])
# Fill in this file with the code from parsing JSON exercise
