import datetime

if __name__ == '__main__':
    print(len([(1, month, year) for year in range(1901, 2001) for month in range(1, 13) if
         datetime.date(year, month, 1).weekday() == 6]))