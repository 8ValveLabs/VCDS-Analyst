import statistics, csv

def averageAF(fName):
    actualArray = []
    actual = open(fName)
    for row in actual:
        converted = float(row)
        if converted < 1.8:
            converted = (float(row) * 14.7)   
            actualArray.append(converted)
    return(round(statistics.mean(actualArray),2))
    actual.close()

def averageTiming(fName):
    actualArray = []
    actual = open(fName)
    for row in actual:
        converted = float(row)
        if converted > 0.0:
            actualArray.append(converted)
    return(round(statistics.mean(actualArray),2))
    actual.close()

def alertAF(fName):
    richArray = []
    leanArray = []
    actual = open(fName)
    for row in actual:
        converted = float(row)
        if converted < 1.2:
            converted = (converted*14.7)
            if (converted) < 11.8:
                richArray.append(round(converted, 2))
            elif (converted) > 15:
                leanArray.append(round(converted, 2))
    actual.close()
    print("The A/F ratio went below 11.8:1 (rich) " + str(len(richArray)) + " times." + "\nThe A/F ratio went above 15 (lean) " + str(len(leanArray)) + " times.")
    print("Ratios that were very rich : " + str(richArray))
    print("Ratios that were very lean : " + str(leanArray))

def alertTiming(fName):
    highArray = []
    actual = open(fName)
    for row in actual:
        converted = float(row)
        if converted > 30:
            highArray.append(converted)
    actual.close()
    print("The Timing Advance went above 30 Degrees " + str(len(highArray)) + " times.\n")
    print("Degrees Logged Above 30 : " + str(highArray))

def openCSV(fName):
    Columns = []
    Rows = []
    units = []
    if (open("config.ini").readline() == "csvistrimmed : no"):
        with open(fName, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(fName, 'w') as fout:
            fout.writelines(data[5:])
        with open("config.ini", 'w') as fout:
            fout.write("csvistrimmed : yes")
    with open(fName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',',)
        line_count = 0
        filteredColumns=[]
        for row in csv_reader:
            if line_count == 0:
                Columns = list(row)
                line_count += 1
            elif line_count == 1:
                units = list(row)
                line_count += 1
            else:
                Rows.append(row)
                line_count += 1
        for i in Columns:
            if str(i) != "":
                filteredColumns.append(i)
        print("Captured Columns : " + str(Columns) + "\nCaptured units : " + str(units) + "\nCaptured Rows : " + str(len(Rows)))
        ctr=0
        lenCtr=0
        filteredRows=[]
        while ctr < len(Rows):
            rowBuilder=[]
            lenCtr=0
            while lenCtr < len(Rows[ctr]):
                if Rows[ctr][lenCtr] != "":
                    rowBuilder.append(Rows[ctr][lenCtr])
                lenCtr+=1
            filteredRows.append(rowBuilder)
            ctr+=1
        print(filteredColumns)
        sensorDict = dict()
        pair1=[]
        modules=[]
        for i in filteredRows:
            lenCtr = 0
            stampCtr = 0
            while lenCtr < len(i) :
                if filteredColumns[lenCtr] == "STAMP":
                    appender=[("STAMP" + str(stampCtr)),i[lenCtr], i[lenCtr+1]]
                    modules.append(appender)
                    stampCtr+=1
                lenCtr+=1
        pair1.append(modules)
        lenCtr=0
        for p in pair1:
            for r in p:
                if r[0] == "STAMP0":
                    print("Module = " +  + r)




averageActual = averageAF("actual.csv")
averageSpecified = averageAF("specified.csv")
print("The Actual A/F Ratio Averaged : " + str(averageActual) + "\nThe Specified A/F Ratio Averaged : " + str(averageSpecified))
print("**** Actual AF ****")
alertAF("actual.csv")
print("**** Specified AF ****")
alertAF("specified.csv")

print("The average timing advance was : " + str(averageTiming("timing.csv")))
alertTiming("timing.csv")
openCSV("RichRest.csv")