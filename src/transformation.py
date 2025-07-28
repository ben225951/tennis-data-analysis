import pandas as pd
import os


#get absolute path
project_root_dir = os.path.dirname(os.path.dirname(__file__))

# Define the raw data folder
raw_data_dir = os.path.join(project_root_dir, 'data', 'raw')

#get a list of all csv files in directory
csv_files = [os.path.join(raw_data_dir,f) for f in os.listdir(raw_data_dir) if f.endswith(".csv")]


#read each csv file and store in list
dfs=[]

for file in csv_files:
    df=pd.read_csv(file)
    dfs.append(df)


#Concatenate the list of DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)


#cleans data
def clean_data(data):

    #drop rows with missing critical values
    critical_cols = [
    'tourney_date',     # match date (for sorting, filtering)
    'winner_name',      # winner's name
    'loser_name',       # loser's name
    ]

    data.dropna(subset=critical_cols, inplace=True)

    #parse dates
    data['tourney_date'] = pd.to_datetime(data['tourney_date'], format='%Y%m%d', errors='coerce')

    #add year column
    data['year'] = data['tourney_date'].dt.year

    #convert numeric columns
    numeric_cols = ['winner_rank', 'loser_rank', 'minutes', 'winner_age', 'loser_age', 'best_of']

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    #drop duplicates
    data.drop_duplicates(inplace=True)


    return data



#saves data into csv for analysis
cleaned_df = clean_data(combined_df)

processed_data_dir = os.path.join(project_root_dir, 'data', 'processed','tennis_cleaned_data.csv')

cleaned_df.to_csv(processed_data_dir, index=False)

