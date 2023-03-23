# Song Plays Aggregator

## Installation

1. Install Python
2. Clone the repo using the following code:
```
    git clone https://github.com/adrianomiranda14/bmat_tt
    cd bmat_tt
```
3. Install required packages
`pip install -r requirements.txt`

## Using the API

1. Run the Flask server
`flask run`

    This will stay running in a terminal, so open a new terminal

2. run `schedule_file.py` and input the file you want to send for processing from the raw files directory. You will receive a filename for the aggregated data.

3. Run `retrieve_file.py` and input the filename of the aggregated data you want to retrieve
