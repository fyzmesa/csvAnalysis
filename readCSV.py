import csv
from tabulate import tabulate
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

def read_csv_file(filename, columns, skip_rows=1):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i % skip_rows == 0:
                if columns is None:
                    data.append(row)
                else:
                    data.append([row[i] for i in columns])
    return data

def count_rows(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
    return row_count

def print_table(data):
    print(tabulate(data, headers='firstrow', tablefmt='grid'))

def plot_data(data):
    x = [datetime.strptime(row[0], '%Y-%m-%d') for row in data[1:]]
    y = [float(row[1]) for row in data[1:]]
    plt.plot(x, y)
    plt.xlabel('2024')
    plt.ylabel('PRICE')
    plt.title('BTCUSD')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.gcf().autofmt_xdate()
    plt.show()

def main():
    start_time = datetime.now()
    # print("Script started at:", start_time.strftime("%Y-%m-%d %H:%M:%S"))
    filename = 'BTCUSD.csv'
    # columns = None # Display all columns
    columns = [0, 4]
    btcdata = read_csv_file(filename, columns, skip_rows=1)
    # print_table(btcdata)
    plot_data(btcdata)
    print("The file contains:", count_rows(filename), "rows")
    end_time = datetime.now()
    # print("Script ended at:", end_time.strftime("%Y-%m-%d %H:%M:%S"))
    execution_time = end_time - start_time
    print("Execution time:", execution_time)
    
if __name__ == '__main__':
    main()
