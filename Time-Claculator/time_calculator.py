def add_time(start_time, duration, start_day = ""):
    # Splitting the start_time into hours, minutes, am_pm
    pieces = start_time.split()
    time = pieces[0].split(":")
    am_pm = pieces[1]

    # Calculate 24-hour clock
    if am_pm == 'PM' :
        hour = int(time[0]) + 12
        time[0] = str(hour)

    # Splitting duration into hours and minutes
    dur_time = duration.split(":")

    # Adding duration to start_time
    new_hour = int(time[0]) + int(dur_time[0])
    new_minutes = int(time[1]) + int(dur_time[1])
    if new_minutes > 60 :
        hours_add = new_minutes // 60
        new_minutes = new_minutes - hours_add * 60
        new_hour = new_hour + hours_add

    # Calculating number of days added according to new_hour
    days_add = 0
    if new_hour > 24:
        days_add = new_hour // 24
        new_hour = new_hour - days_add * 24

    # Calculating next day or n days later
    if days_add > 0 :
        if days_add == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(days_add) + " days later)"
    else :
        days_later = ""

    # Find AM or PM
    # Return to 12-hour clock format
    if new_hour > 0 and new_hour < 12 :
        am_pm = "AM"
    elif new_hour == 12 :
        am_pm = "PM"
    elif new_hour > 12 :
        am_pm = "PM"
        new_hour = new_hour - 12
    else : # new_hour == 0
        am_pm = "AM"
        new_hour = new_hour + 12

    # Calculating days of the week
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_days_lower = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    if start_day :
        weeks = days_add // 7
        start_day = start_day.lower()
        i = week_days_lower.index(start_day) + (days_add - 7 * weeks)

        i = i % 7
        day = ", " + week_days[i]
    else :
        day = ""

    # Finally putting everything together and Calculating new time
    new_time = str(new_hour) + ":" + \
        (str(new_minutes) if new_minutes > 9 else("0" + str(new_minutes))) + \
        " " + am_pm + day + days_later


    return new_time
