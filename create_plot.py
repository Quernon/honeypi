import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

str2date = lambda x: datetime.strptime(x.decode("utf-8"), '%Y-%m-%d %H:%M') #Used to convert first column of data from string to datetime type.

headers = ['Date&Time', 'Temperature (°C)', 'Humidity (%)']

def read_data(filename):
    data  = pd.read_csv(filename, names=headers)
    return data


def create_plot(filename, row_nos, output_file):
    data = read_data(filename)
    data['Date&Time'] = pd.to_datetime(data['Date&Time']) #Convert string to pandas timestamp
    #Assign columns to separate arrays.
    x = data[headers[0]]
    y1 = data[headers[1]]
    y2 = data[headers[2]]

    if row_nos > 0:
        x = x.tail(row_nos)
        y1 = y1.tail(row_nos)
        y2 = y2.tail(row_nos)

    #Plotting to plot with pyplot
    #Create figure and define first series
    fig, ax1 = plt.subplots()
    ax1.plot(x, y1, 'b-')
    ax1.set_xlabel('Date & Time')
    ax1.set_ylabel('Temperature (°C)', color='b')
    ax1.tick_params('y', colors='b')

    #Define second series
    ax2= ax1.twinx()
    ax2.plot(x, y2, 'r-')
    ax2.set_ylabel('Humidity (%)', color='r')
    ax2.tick_params('y', colors='r')

    #Autoformat x axis for datetime, tighten layout and output to png
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.savefig(output_file)

#Plot using all data
create_plot('/home/pi/logs/mqtt.log', 0, '/var/www/html/plots/hiveA_all.png')

#Plot of last 6 hours
create_plot('/home/pi/logs/mqtt.log', 24, '/var/www/html/plots/hiveA_6h.png')

#Plot of last 24 hours
create_plot('/home/pi/logs/mqtt.log', 96, '/var/www/html/plots/hiveA_24h.png')

#Plot of last 3 days
create_plot('/home/pi/logs/mqtt.log', 288, '/var/www/html/plots/hiveA_3d.png')

#Plot of last week
create_plot('/home/pi/logs/mqtt.log', 672, '/var/www/html/plots/hiveA_1w.png')
