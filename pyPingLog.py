from pythonping import ping
import time
from datetime import datetime
import csv

# Pfad zur Logdatei
Path = "C:/temp/"


def main():
    filepath = Path + datetime.now().strftime("%d%m%Y") + ".csv"
    with open(filepath, 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        response = ping("satsa0030").rtt_avg_ms
        ttime = datetime.now().strftime("%H:%M:%S")
        writer.writerow([ttime, str(response).replace(".", ",")])
    time.sleep(2)
    main()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
