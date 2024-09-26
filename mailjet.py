"""
This call sends a message based on a template.
"""
from mailjet_rest import Client
import os
api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_SECRET']
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
				{
						"From": {
								"Email": "harborcityhockeyclub@dwboygenius.com",
								"Name": "HCH Fall"
						},
						"To": [
								{
										"Email": "dwboygenius@gmail.com",
										"Name": "DW Test"
								}
						],
						"TemplateID": 1,
						"TemplateLanguage": True,
						"Subject": "HCHC test"
				}
		]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())