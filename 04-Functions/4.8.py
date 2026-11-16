
def time_string(hours, minutes, time_format):
    time = ""

    if time_format == '12':
        if hours < 12:
            period = "am"
        else:
            period = "pm"

        if hours == 0:
            hours = 12
        elif hours > 12:
            hours = hours - 12

        hours = str(hours)
        minutes = str(minutes).zfill(2)
        time = hours + ":" + minutes + period

    elif time_format == '24':
        hours = str(hours).zfill(2)
        minutes = str(minutes).zfill(2)
        time = hours + ":" + minutes

    return time


print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 7, '12'))
print(time_string(13, 10, '12'))
