import csv
t=25
Filepath = 'charge_sch.csv'
def Busread (Filepath):
    print("hello")
    file = open(Filepath)
    type(file)

    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)
    print("header is", header)

    Bus={}
    rows = []
    bus_count=0
    for row in csvreader:
            bus_count=bus_count+1
            bus_counts=str(bus_count)
            rows.append(row)
            L=len(row)
            Bus[bus_counts]={}
            for i in range(1,L+1):
                if i==1:
                    data_key='id'
                elif i==2:
                    data_key = 'soc'
                elif i==3:
                    data_key='hh'
                elif i==4:
                    data_key='mm'
                elif i==5:
                    data_key = 'charger_loc'
                else:
                    print("Parameter other than bus_id, soc, hours:minutes, Charger Location")
                Bus[bus_counts][data_key]=row[i-1]

    print(rows)
    print(Bus)
    print("Bus Charge Information Completed")
    return Bus