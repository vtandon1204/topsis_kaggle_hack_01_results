import gspread
import csv
from google.oauth2.service_account import Credentials

# Path to your service account JSON key file
SERVICE_ACCOUNT_FILE = "kagglehack01results-b75d33fcecf0.json"

# Define the required scopes
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate using the service account
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("Kaggle_Hack_01_results").sheet1  # Replace with your Google Sheet name

# Path to your CSV file
CSV_FILE_PATH = "kaggle_hack_01_results.csv"

# Function to upload CSV data to Google Sheet
def upload_csv_to_sheet(csv_file_path, sheet):
    with open(csv_file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
        
        # Clear existing data in the sheet
        sheet.clear()
        
        # Update the sheet with the new data
        sheet.update("A1", data)  # Start updating from the first cell

# Call the function
upload_csv_to_sheet(CSV_FILE_PATH, sheet)

print("CSV data successfully uploaded to the Google Sheet!")
