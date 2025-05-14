jobs = [
    {'title':"python developer","exp_date":"2025-04-25"},
    {'title':"java developer","exp_date":"2025-05-25"},
    {'title':"data analyst","exp_date":"2025-06-25"},
    {'title':"data scientist","exp_date":"2025-07-25"},
    {'title':"web developer","exp_date":"2025-08-25"},
    {'title':"android developer","exp_date":"2025-09-25"},

]
import datetime
def exp(): 
    print("\n Jobs ")
    for job in jobs:
        title = job["title"]
        exp_date=datetime.datetime.strptime(job["exp_date"],"%Y-%m-%d")
        to= datetime.datetime.now()
        if exp_date>=to:
            print(f"Job:{title}-------->Available")
        else:
            print(f"Job:{title}--------->Expired")


exp()
