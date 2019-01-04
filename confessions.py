import time ,sys, gspread, csv
from datetime import date, time, datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc =  gspread.authorize(credentials)
spreadsheet_id = "19dkFElbGBplq0ngMuShJaQqMzDO0_JIpL88YXsJjzB0"


worksheet = gc.open("UC Berkeley Confessions Responses").sheet1
confessions = worksheet.get_all_values()

#service = discovery.build('sheets', 'v4', credentials=credentials)
#confessions = service.spreadsheets().values().batchGet(spreadsheetId = spreadsheet_id)


#Array of posting times in datetime objects

def makeFile(row):
    file_name = "test.csv"
    date = confessions.row_values(row)[0].encode("utf-8")
    conf = confessions.row_values(row)[1].encode("utf-8")
    with open(file_name, "a") as readFile:
        reader = csv.writer(readFile)
        reader.writerow([row, conf, date])
    print conf

#  
def weeklyGenerator(startDate):
    file_name = "week.csv"
    length = len(confessions)

    #Initializing variables for time between posts and starting time for posts
    delta = timedelta(minutes = 90)
    startTime = time(hour = 8, minute = 0)
    with open(file_name, "a") as readFile:
        reader = csv.writer(readFile)

        #Converts date input from string to datetime object
        date = datetime.strptime(startDate, '%m/%d/%y')
        #Creates datetime object with first posting time 
        postDate = datetime.combine(date, startTime)

        for row in range(70, 0, -1):
            number = length - row
            conf = confessions[number][1].encode("utf-8")
            reader.writerow([number, postDate.strftime("%m %d %Y %H:%M"), conf])
            if postDate.hour == 21:
                #If on last post time of the day (9:30 pm), wrap around to new day
                postDate += timedelta(hours = 10, minutes = 30)  
            else:
                #Otherwise add 90 minutes
                postDate += delta


            


weeklyGenerator("1/4/19")
#makeFile(sys.argv[1])
#print confessions.row_values(sys.argv[1])[1].encode("utf-8")
