import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib.pyplot as plt

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'path_to_json_file.json', scope)

# Authenticate and open the Google Sheets document
client = gspread.authorize(credentials)
spreadsheet = client.open('Your Google Sheet Name')

# Select the worksheet you want to work with
# Replace 0 with the appropriate index of your worksheet
worksheet = spreadsheet.get_worksheet(0)

# Retrieve the data and convert it into a Pandas DataFrame
data = worksheet.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)

# Manipulate the data as per your requirements
# For example, you can filter the data based on a condition
filtered_data = df[df['Team'] == 'New England Patriots']

# Generate a bar graph of cap space for the filtered data
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['Team'], filtered_data['Cap Space'])
plt.xlabel('Team')
plt.ylabel('Cap Space')
plt.title('NFL Team Cap Space - New England Patriots')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Update the Google Sheets document with the new data
worksheet.update('A1', [headers] + df.values.tolist())
