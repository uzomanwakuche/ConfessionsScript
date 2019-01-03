import sys, gspread, csv
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc =  gspread.authorize(credentials)

confessions = gc.open("UC Berkeley Confessions Responses").sheet1

# Extract and print all of the
values_list = confessions.row_values(3426)[1]


def makeFile(row):
    file_name = "test.csv"
    date = confessions.row_values(row)[0].encode("utf-8")
    conf = confessions.row_values(row)[1].encode("utf-8")
    with open(file_name, "a") as readFile:
        reader = csv.writer(readFile)
        reader.writerow([row, conf, date])
    print conf

makeFile(sys.argv[1])
#print confessions.row_values(sys.argv[1])[1].encode("utf-8")
