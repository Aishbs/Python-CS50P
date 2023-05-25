months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    #Input date from User
    date = input("Date: ")


    if '/' in date:
        #Spliting date
        m, d, y = date.split('/')

        try:
            if (1 <= int(m) <= 12) and (1 <= int(d) <= 31):
                break
        except:
            pass

    elif ',' in date:

        try:
            #Spliting date
            old_mon, old_date, y = date.split(" ")
            for i in range(len(months)):
                if old_mon == months[i]:
                    m = i + 1

            d = old_date.replace(',','')

            if (1 <= m <= 12) and (1 <= int(d) <= 31):
                break

        except:
            print()
            continue

print(f"{y.strip(' ')}-{int(m):02}-{int(d):02}")