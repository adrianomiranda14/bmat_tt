import requests

filename = input("Type filename from API")
response = requests.get(f"http://localhost:8000/download_result/{filename}")
filepath = input('Type desired file path')

with open(str(filepath) + "csv", "wb") as file:
    file.write(response.content)

print(f"Result saved to {filepath}.csv")
