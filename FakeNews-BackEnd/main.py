import requests

data = {'input_data': ['Bush died']}
response = requests.post('http://localhost:5000/predict', json=data)
print(response.json())
