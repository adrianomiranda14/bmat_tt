import requests

filename = input("Type raw filename (e.g. day1.csv)")

with open(f"raw_files\{filename}", "rb") as file:
    response = requests.post(
        "http://localhost:5000/schedule_processing/",
        files={"file": file},
        data={"filename": filename}
    )

saved_filename = response.text
print("Filename:", saved_filename)