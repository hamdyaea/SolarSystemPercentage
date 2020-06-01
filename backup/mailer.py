#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com
# Send the result of the aide software via e-mail

from mailjet_rest import Client
import os
api_key = 'e4f0f77b8d018813623d4290b9a73101'
api_secret = '2b6c3935a0e1ba19879f66c58ec09e88'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

with open('/root/aide_result', 'r') as myfile:
    datatext = myfile.read()

data = {
  'Messages': [
    {
      "From": {
        "Email": "hamdy.aea@protonmail.com",
        "Name": "Daylight Linux Centos 8 Server"
      },
      "To": [
        {
          "Email": "hamdy.aea@gmail.com",
          "Name": "Hamdy"
        }
      ],
      "Subject": "Daylight Linux AIDE check",
      "TextPart": datatext,
      #"CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
