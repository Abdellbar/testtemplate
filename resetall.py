import requests

visionbots =  [
			'visionbotai1',
			'visionbotai2',
			'visionbotai3',
			'visionbotai4',
			'visionbotai5',
			'visionbotai6',
			'visionbotai7',
			'visionbotai8'
		]
for bot in visionbots:
	url='https://'+bot+'.herokuapp.com/reset'
	response = requests.get(url)
	print("reset for "+bot+" returned response "+str(response.status_code))