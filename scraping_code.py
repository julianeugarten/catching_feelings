import AO3
import csv
import os
import pandas as pd
import time
from tqdm import tqdm

# Open your CSV with fic IDs
# The fic IDs should be in a column labeled 'ID'
df = pd.read_csv('file_path_csv')

# Transform IDs to list
ID_list = df['ID'].tolist()
AO3.utils.limit_requests()

results_folder = 'results'
os.makedirs(results_folder, exist_ok=True) 

# Load the last processed ID from a file
last_processed_id_file = os.path.join(results_folder, 'last_processed_id.txt')
last_processed_id = None

if os.path.exists(last_processed_id_file):
    with open(last_processed_id_file, 'r') as f:
        last_processed_id = f.readline().strip()

if last_processed_id:
    try:
        last_processed_index = ID_list.index(int(last_processed_id))
        ID_list = ID_list[last_processed_index + 1:]  # Start from the next ID
    except ValueError:
        print("Last processed ID not found in the ID list.")

with open(os.path.join(results_folder, 'file.csv'), 'a', newline='', encoding='utf-8') as f:  # Use 'a' to append
    writer = csv.writer(f)

    for ID in ID_list:
        try:
            work = AO3.Work(ID)
            comments = work.get_comments()
            for comment in comments:
                text = comment.text  # Access the 'text' attribute
                writer.writerow([ID, text])
        except Exception as e:
            print(f"An unexpected error occurred for ID {ID}: {e}")
            if "rate-limited" in str(e):
                print("Pausing for 2 minutes before retrying...")
                time.sleep(120)  # Pause for 2 minutes
                # Reload the list of IDs after the pause
                df = pd.read_csv('work_ids.csv', sep=',')
                ID_list = df['ID'].tolist()
        finally:
            # Write the ID to the file even if an error occurs
            with open(last_processed_id_file, 'w') as f:
                f.write(str(ID) + '\n')  # Add a new line after each ID
