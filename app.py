import os
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, send_from_directory, abort
from task_1 import process_csv

app = Flask(__name__)
storage_path = "uploaded_files/"
result_path = "result_files/"

executor = ThreadPoolExecutor(max_workers=4)

def process_file(input_file, output_file):
    process_csv(input_file, output_file)

@app.route('/schedule_processing/', methods=['POST'])
def schedule_processing():
    if 'file' not in request.files:
        abort(400, 'No file part')
    
    if 'filename' not in request.form:
        abort(400, 'No filename provided')

    file = request.files['file']
    filename = request.form['filename']
    input_file_path = os.path.join(storage_path, filename)
    output_file_path = os.path.join(result_path, filename)

    os.makedirs(storage_path, exist_ok=True)
    os.makedirs(result_path, exist_ok=True)

    file.save(input_file_path)

    executor.submit(process_file, input_file_path, output_file_path)

    return filename

@app.route('/download_result/<filename>', methods=['GET'])
def download_result(filename):
    result_file = os.path.join(result_path, filename)

    if not os.path.exists(result_file):
        abort(404, 'Result not found or not ready')
    return send_from_directory(result_path, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
