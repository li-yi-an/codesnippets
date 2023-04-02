day=1
mth=str(input("enter month(e.g. jan): ")).capitalize()
year=int(input("enter year(e.g. 2023): "))
start_day_dic = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",0:"Saturday"}
months = {"Jan":31,"Feb":28,"Mar":31,"Apr":30,"May":31,"Jun":30,"Jul":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}
int_month=int(list(months).index(mth)+1)

years_since=0
months_since=0
days_since=0
def days_since():
    #set days since 1/1/1 as 0
    years_since=sum(list(months.values()))*(year-1)
    months_since=0
    for i in range(list(months).index(mth)):
        months_since+=list(months.values())[i]
    days_since=day
    return (years_since+months_since+days_since)

def isLeapYear():
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def leap_year_ctr():
    leap_year_counter=0
    for y in range(3,year):
        if y%4==0:
            if y%100==0:
                if y%400==0:
                    leap_year_counter+=1
                else:
                    continue
            else:
                leap_year_counter+=1
        else:
            continue
    return leap_year_counter
    

days_since_1=days_since()+leap_year_ctr()+1

def dayofweek():
    if isLeapYear() and int_month>2:
        return start_day_dic[(days_since_1+1)%7]
    else:
        return start_day_dic[(days_since_1)%7]

spacesInCalendar=list(start_day_dic.values()).index(dayofweek())


#day in month
daysInMonth=months[mth]
if isLeapYear() and int_month==2:
    daysInMonth+=1

def printCalendar(spacesInCalendar,mth,year,days):
    print(f"{mth} {year}")
    print("Sun Mon Tue Wed Thu Fri Sat")
    for i in range(spacesInCalendar):
        print("    ",end="")
    newLine=spacesInCalendar
    for date in range(days):
        print(f"{date+1:>3} ",end="")
        newLine+=1
        if newLine%7==0:
            print("\n")

    
printCalendar(spacesInCalendar,mth,year,daysInMonth)