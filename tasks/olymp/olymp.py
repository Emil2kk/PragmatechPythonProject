import datetime
start_date = datetime.date(2022, 2, 22)
first_date=datetime.date(2022,2,24)
end_date = datetime.date(2100, 12, 30)
delta = datetime.timedelta(days=1)

while start_date <= end_date:
    start_date += delta
    seq = int(start_date.strftime("%Y%m%d"))
    y=str(seq)
    if y==y[::-1]:
        minus=start_date-first_date
        print(minus)
        
            
    
    
    
 