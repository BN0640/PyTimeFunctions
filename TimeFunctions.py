def correctTime(hour = int, minute = int, second = int, millisecond = int):
    # --------------------------------------------------------------------------------------------------- #
    # This function gets some time units as parameters and return them correcting values above the limit  #
    # Example:                                                                                            #
    #   input: 00:70:00.000 --> this is 70 minutes                                                        #
    #   output: 01:10:00.000 --> this is 1 hour and 10 minutes                                            #
    # --------------------------------------------------------------------------------------------------- #

    if millisecond >= 1000:
        while millisecond >= 1000:
            millisecond -= 1000
            second += 1
    if second >= 60:
        while second >= 60:
            second -= 60
            minute += 1
    if minute >= 60:
        while minute >= 60:
            minute -= 60
            hour += 1
    return hour, minute, second, millisecond

def deFormatTime(time = str):
    # --------------------------------------------------------------------------------------------------- #
    # This function gets formated time as parameters and return them in variables                         #
    # Example:                                                                                            #
    #   input: 01:02:03.500                                                                               #
    #   output: Hour: 1, Minute = 2, Seconds = 3, Milliseconds: 500                                       #
    # --------------------------------------------------------------------------------------------------- #

    values = time.split(':')

    hour = values[0]
    minute = values[1]
    second = values[2]
    second, millisecond = second.split('.')

    hour = int(hour)
    minute = int(minute)
    second = int(second)
    millisecond = int(millisecond)

    hour, minute, second, millisecond = correctTime(hour, minute, second, millisecond)

    return hour, minute, second, millisecond

def FormatTime(hour = 0, minute = 0, second = 0, millisecond = 0):
    # --------------------------------------------------------------------------------------------------- #
    # This function gets time units as parameters and return them formated                                #
    # Example:                                                                                            #
    #   input: Hour: 1, Minute = 2, Seconds = 3, Milliseconds: 500                                        #
    #   output: 01:02:03.500                                                                              #
    # --------------------------------------------------------------------------------------------------- #

    hour, minute, second, millisecond = correctTime(hour, minute, second, millisecond)

    if hour < 10:
        hour = f'0{hour}'
    if minute < 10:
        minute = f'0{minute}'
    if second < 10:
        second = f'0{second}'
    if millisecond < 10:
        millisecond = f'00{millisecond}'
    elif millisecond < 100:
        millisecond = f'0{millisecond}'

    return f'{hour}:{minute}:{second}.{millisecond}'

def calcTime(mode = str,time1 = str, time2 = str):
    # --------------------------------------------------------------------------------------------------- #
    # This function gets 2 formated times as parameters and a mode to add or subtract the times           #
    # Example:                                                                                            #
    #   input: '+' 01:20:20.000 01:03:50.000                                                              #
    #   output: 02:24:10.000                                                                              #
    #   input: '-' 01:00:00.000 00:00:00.001                                                              #
    #   output: 00:59:59.999                                                                              #
    # --------------------------------------------------------------------------------------------------- #

    hour1, minute1, second1, millisecond1 = deFormatTime(time1)
    hour2, minute2, second2, millisecond2 = deFormatTime(time2)
    if mode == '+':
        hour = hour1 + hour2
        minute = minute1 + minute2
        second = second1 + second2
        millisecond = millisecond1 + millisecond2
    elif mode == '-':
        hour = hour1 - hour2
        minute = minute1 - minute2
        second = second1 - second2
        millisecond = millisecond1 - millisecond2
        if millisecond < 0:
            second -= 1
            millisecond = 1000 + millisecond
        if second < 0:
            minute -= 1
            second = 60 + second
        if minute < 0:
            hour -= 1
            minute = 60 + minute
    else:
        print('[CalcTime] ERROR: "mode" is out of range')

    return FormatTime(hour, minute, second, millisecond)

while True:
    result = FormatTime(1,1,1,1)
    
    print(result)
    
    break
    
    #print(f'Hours: {hour}, Minutes: {minute}, Seconds: {second}, Milliseconds: {millisecond}')
    #print(f'{hour} Hours, {minute} Minutes, {second} Seconds, {millisecond} Milliseconds')
    #print(f'New Time:{newTime}')