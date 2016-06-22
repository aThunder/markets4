# stkVolumeAllTests.py

'''
    1. Is called by ControlStkVolumeB3.py (along with data applicable to choice made in ControlStkVolumeB3.py
    2. Calls buildSeriesM.py to retrieve dataframe for applicable symbol & data range
    3. Performs 1 of 3 volume calculations (depending on info from ControlStkVolumeB3.py):
            a. Volume Up/Down
            b. Volume Moving Averages
            c. Volume Stock:Mkt Ratios
'''

import sqlite3
import pandas as pd
import numpy as np
import buildSeriesM
# import matplotlib.pyplot as plt
# from sqlalchemy import create_engine

##########################################
class SetSpan():

    def __init__(self, daysAvailable):
        # self.symbol = symbol
        self.daysAvailable = daysAvailable
        # print("Days Available: ", self.daysAvailable)

    def specifySpanMovAvg(self):
        try:
            print()
            self.movAvgLen = int(
                input("Moving Average Length (1-{0})? ".format(self.daysAvailable)))
            self.movAvgLenN = self.movAvgLen * -1
            print()
            if self.movAvgLen <= self.daysAvailable:
                print("OK, {0} is a valid moving average length".format(self.movAvgLen))
                # print("ENDING DATE: ", self.endDate)
                # print("Returning Now...")
                return self.movAvgLen
            else:
                print("{0} is NOT a valid moving average length. TRY AGAIN".format(self.movAvgLen))
                SetSpan.specifySpanMovAvg(self)
        except:
            print()
            print("THAT WASN'T EVEN A NUMBER...TRY AGAIN")
            SetSpan.specifySpanMovAvg(self)

    def specifySpanReport(self):
        self.daysToReport = int()
        try:
            self.movAvgLen
        except:
            self.movAvgLen = 0
        # print("MovAvgLenTest: ",self.movAvgLen)
        try:
            print()
            self.daysToReport = int(
                input("How Many Days To Include In Report (1-{0})? ".format(self.daysAvailable - self.movAvgLen)))
            self.daysToReportN = self.daysToReport * -1
            print()
            if self.daysToReport <= (self.daysAvailable-self.movAvgLen):
                print("OK, {0} is a valid report length".format(self.daysToReport))
                # print("ENDING DATE: ", self.endDate)
                print()
                # print("self.daysToReport to be returned: ", self.daysToReport)
                # print("Type: ",type(self.daysToReport),self.daysToReport)
            else:
                print("{0} is NOT a valid report length. TRY AGAIN".format(self.daysToReport))
                SetSpan.specifySpanReport(self)
        except:
            print()
            print("THAT WASN'T EVEN A NUMBER...TRY AGAIN")
            SetSpan.specifySpanReport(self)

    def returnSpanReport(self):
        return self.daysToReport
    def returnSpanMovAvg(self):
        return self.movAvgLen


#########################
#########################
# def main(daysAvailable,spanType):
#     a = SetSpan(daysAvailable)
#     if spanType == 'movavg':
#         a.specifySpanMovAvg()
#         movAvgLen = a.returnSpanMovAvg()
#         return movAvgLen
#     elif spanType == 'report':
#         a.specifySpanReport()
#         reportLen = a.returnSpanReport()
#         return reportLen

def spanMovAvg(daysAvailable):
    a = SetSpan(daysAvailable)
    a.specifySpanMovAvg()
    movAvgLen = a.returnSpanMovAvg()
    # print(movAvgLen) ## standalone testing
    return movAvgLen

def spanReport(daysAvailable):
    a = SetSpan(daysAvailable)
    a.specifySpanReport()
    reportLen = a.returnSpanReport()
    # print(reportLen) ## standalone testing
    return reportLen

## for standalone testing
# if __name__ == '__main__': main(319,'movavg')
# if __name__ == '__main__': main(319,'movavgreport')
if __name__ == '__spanMovAvg': spanMovAvg(300)
if __name__ == '__spanReport': spanReport(300)