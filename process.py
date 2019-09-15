import statistics
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
        if converted < 1.8:
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


averageActual = averageAF("actual.csv")
averageSpecified = averageAF("specified.csv")
print("The Actual A/F Ratio Averaged : " + str(averageActual) + "\nThe Specified A/F Ratio Averaged : " + str(averageSpecified))
print("**** Actual AF ****")
alertAF("actual.csv")
print("**** Specified AF ****")
alertAF("specified.csv")

print("The average timing advance was : " + str(averageTiming("timing.csv")))
alertTiming("timing.csv")