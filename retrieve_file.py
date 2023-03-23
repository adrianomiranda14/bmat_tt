import requests

# Download the result
response = requests.get(f"http://localhost:8000/download_result/{task_id}")

with open("result.csv", "wb") as file:
    file.write(response.content)

print("Result saved to result.csv")
