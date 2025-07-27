# Downloads raw data from Jeff Sackmann’s tennis data repo

import os
import requests
import pandas as pd

# common starting part used to build full URL
# by appending specific filenames or paths
base_url = "https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/"


#get absolute path
project_root_dir = os.path.dirname(os.path.dirname(__file__))

# Define the raw data folder
raw_data_dir = os.path.join(project_root_dir, 'data', 'raw')

# creates the folder if it doesn't exist
# don't give an error if it exists
os.makedirs(raw_data_dir, exist_ok=True)



# get current year dynamicaly
# current_year = datetime.now().year
current_year=2024


# downloads and saves csv 
def download_file(filename):

    # completes url to download csv from
    url = base_url + filename

    # constructs a full file path
    # avoids manual string concatenation, cross platform issues
    path = os.path.join(raw_data_dir, filename)


    # creates the folder if it dosent't exist
    # extracts the directory part from full file path
    os.makedirs(os.path.dirname(path), exist_ok=True)


    # downloads file from URL and saves it locally, with error handling
    # prevents crashing, better debugging, issues are handled gracefully

    try:
        # fetches file from website
        # file content is in bytes
        response = requests.get(url)

        # raises exceptions instead of returning error page
        # prevents saving bad/empty files
        response.raise_for_status()

        #creates/opens file for writing binary data 
        with open(path, 'wb') as f:
            f.write(response.content)


        print(f"✅ Downloaded: {filename}")

    except Exception as e:

        print(f"❌ Failed: {filename} — {e}")


# Ingest main tour matches from 2000 onwards
for year in range(2000, current_year + 1):
    download_file(f"atp_matches_{year}.csv")

