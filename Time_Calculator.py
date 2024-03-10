import re
import string
import math
def add_time(start, duration, today=''):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    endMsg = ""
    # Convert the input today to correct format
    today = today.lower()
    today = today.title()  # capitalize first letter
  
    # Check if 'today' is not empty and is in the 'days' list
    if today and today in days:
        day_index = days.index(today)

    # Patterns to extract hours, minute, AM PM
    hrPattern = '\d+[:]'
    mnPattern = ':[\d]+'
    ampmPattern = '\w[M]'

    hrNow = re.findall(hrPattern, start)[0][:-1]
    mnNow = re.findall(mnPattern, start)[0][1:]
    ampmNow = re.findall(ampmPattern, start)[0]

    extraHr = re.findall(hrPattern, duration)[0][:-1]
    extraMn = re.findall(mnPattern, duration)[0][1:]

    extraHr = int(extraHr)
    extraMn = int(extraMn)
    
    addedMn = int(mnNow) + int(extraMn)
    
    if addedMn >= 60:
        extraHr += 1

    addedHr = int(hrNow) + int(extraHr)
    
    newMn = addedMn % 60
    newHr = addedHr % 12 

    # Since 00 AM/PM is 12 AM/PM
    if newHr == 0:
        newHr = 12

    
    if addedHr >= 12:
        
        addedDays = int(addedHr/24) if ampmNow[0] == 'A' else int(addedHr/24)+1

        if today:
            day_index += addedDays
            day_index = day_index%7

        # If exceed 1 day
        if addedDays >= 1:
            endMsg += " (next day)" if addedDays == 1 else " (" + str(addedDays) + " days later)" 
  
        for _ in range(int(addedHr/12)):
            ampmNow = ampmNow.replace('A','P') if ampmNow[0] == 'A' else ampmNow.replace('P','A')
        
    # Add 0 to single digit minute
    if newMn%10 == newMn:
        newMnStr = "0" + str(newMn)
    else:
        newMnStr = str(newMn)

    # Output new time
    new_time = str(newHr) + ":" + newMnStr + " " + ampmNow
    if today:
        new_time += ", " + days[day_index]
    
    new_time += endMsg

    print(new_time) 
    return new_time

add_time('11:59 PM', '24:05')
