def main():
    # Input time from user
    time = input('What time is it? ')
    # Assigning convert time to variable
    t = convert(time)
    #Print meal time
    if 7.0 <= t <= 8.0:
        print('breakfast time')
    elif 12.0 <= t <= 13.0:
        print('lunch time')
    elif 18.0 <= t <= 19.0:
        print('dinner time')
    else:
        print(end='')

# Convert time into decimal hours
def convert(time):
    if " " in time:
        hr_min, pm_am = time.split(' ')
        hour, minutes = hr_min.split(':')
        if pm_am == 'p.m.' and int(hour) != 12:
            hour = int(hour) + 12
    else:
         hour, minutes = time.split(':')

    hours = float(hour) + float(minutes) / 60
    return hours

if __name__ == "__main__":
    main()