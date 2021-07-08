import json
dosya = open("myfile.json", "r")
json_dosya= json.load(dosya)
print("{}\n{}" .format(json_dosya["kimlik"]["Ad"],json_dosya["kimlik"]["Soyad"]))
# Fill in this file with the code from parsing JSON exercise
