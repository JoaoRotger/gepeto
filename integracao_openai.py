import os
import openai
import json


with open("conf.json", "r") as conf:
    json_conf = json.load(conf)
    apiKey = json_conf["keys"][0]
    org = json_conf["keys"][1]

openai.organization = org
openai.api_key = os.getenv(apiKey)
openai.Model.list()


#org = org-hs57WO5XbA10vS3bAy74Dc9j
