#pip install psaw       
import datetime as dt  
from psaw import PushshiftAPI    #library Pushshift
import time
from datetime import datetime, timedelta
import csv
days_to_subtract=7

api = PushshiftAPI() 

sub='COVID19'
def commendDownload(sub):
    output=[]
    visited=[]

    end_time = datetime.today()
    start_time=end_time - timedelta(days=days_to_subtract)
    C=''
    while(start_time>dt.datetime(2016, 1, 1)):
        print(sub,start_time)
        posts = list(api.search_comments(subreddit=sub,after=int(start_time.timestamp()),before=int(end_time.timestamp()),limit=2000))          ##Max number of posts
        end_time=start_time
        start_time=start_time=end_time - timedelta(days=days_to_subtract)


        for p in posts:
            row=[]
            try:
                row.append(p.author)
                row.append(p.body)
                row.append(p.created_utc)
                row.append(p.subreddit)
                row.append(p.permalink)
                if hasattr(p,'author_flair_text'):
                    row.append(p.author_flair_text)
                else:
                    row.append('')
                output.append(row)
                visited.append(p.permalink)
                C=p.created_utc
            except:
                continue
        time.sleep(1)
    print(sub,len(output),C)
    with open(sub+'.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in output:
            employee_writer.writerow(row)


subs=['AskDocs','medical_advice','medical']
for s in subs:
    commendDownload(s)