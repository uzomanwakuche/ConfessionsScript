import time ,sys, gspread, csv
import pytz
from datetime import date, time, timedelta, datetime
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
    print (conf)

#  
def weeklyGenerator(startDate, count, startNumber):
    file_name = "week.csv"
    length = len(confessions)

    #Initializing variables for time between posts and intial start time
    delta = timedelta(minutes = 90)
    startTime = time(hour = 8, minute = 0)
    with open(file_name, "w", encoding="utf-8") as readFile:
        reader = csv.writer(readFile)
        date = datetime.strptime(startDate, "%m/%d/%y") #Converts input date to datetime object

        postDate = datetime.combine(date, startTime).astimezone(pytz.utc) #Creates datetime object with initial posting time (in UTC)

        for row in range(count, 0, -1):
            count = length - row   #Finds appropriate row number of spreadsheet
            conf = str(startNumber) + ". " + confessions[count][1] #Pulls Confession from spreadsheet and appends confession number to it
            unix = postDate.timestamp()
            reader.writerow([count, postDate.strftime("%m %d %Y %H:%M"), conf, unix])
            if postDate.hour == 5:  #If on last post time of the day 9:30pm (5:30 am UTC), jump to 8am next day (4pm UTC)
                postDate += timedelta(hours = 10, minutes = 30)  
            else:
                postDate += delta #Otherwise add 90 minutes
            startNumber += 1


            


weeklyGenerator("1/10/19", 1, 1250)
weeklyGenerator(sys.argv[1],int(sys.argv[2]), int(sys.argv[3]))
#makeFile(sys.argv[1])
#print confessions.row_values(sys.argv[1])[1].encode("utf-8")
