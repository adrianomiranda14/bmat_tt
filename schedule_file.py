import requests

filename = "example_play_data_aggregated.csv"

with open("raw_files\example_play_data.csv", "rb") as file:
    response = requests.post(
        "http://localhost:5000/schedule_processing/",
        files={"file": file},
        data={"filename": filename}
    )

saved_filename = response.text
print("Filename:", saved_filename)