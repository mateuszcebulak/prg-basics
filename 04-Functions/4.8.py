def time_string(hours, minutes, time_format):
    time = " "
    if time_format == 12:
        
        if hours <= 12:
            hours = str(hours)
            minutes = str(minutes)
            time = hours + " " + minutes
        else:
            time_hours = str(hours - 12)
            time_minutes = str(minutes)
            time = hours + " " + minutes
            
    elif time_format == 24:
        hours = str(hours)
        minutes = str(minutes)
        time = hours + " " + minutes
    return time

