import os
#import openai
import json
import requests


'''with open("conf.json", "r") as conf:
    json_conf = json.load(conf)
    apiKey = json_conf["keys"][0]
    org = json_conf["keys"][1]
'''
#openai.organization = org
#openai.api_key = os.getenv(apiKey)
#openai.Model.list()

with open("parameters.json", "r") as parameters:
    parameter = json.load(parameters)
    model = parameter['model']
    prompt = parameter['prompt']
    max_tokens = parameter['max_tokens']
    temperature = parameter['temperature']
    top_p = parameter['top_p']
    n = parameter['n']
    stream = parameter['stream']
    logprobs = parameter['logprobs']
    stop = parameter['stop']

url = "https://api.openai.com/v1/models"

payload = {}
headers = {
  'Authorization': 'Bearer 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'
}

response = requests.request("GET", url, headers=headers, data=payload)

#with open("resultado.json", "w") as file:
#    resultado = response.json()
#    json.dump(resultado, file)



#org = org-hs57WO5XbA10vS3bAy74Dc9j
