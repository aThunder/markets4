import datetime

class CreateReportTxtFile():
    # def __init__(self,choice1,results):

    def setParameters(self, choice1, results):
        self.resultsCart = results

        if choice1 == 'c':
            self.choice1 = 'Created '
            self.fileWrite = open('reports/Rpt{0}VOLUME{1}.txt'.
                             format(self.resultsCart['Symbol'],
                             self.resultsCart['Date']), 'w')
        elif choice1 == 'a':
            self.choice1 = 'Updated '
            self.fileWrite = open('reports/Rpt{0}VOLUME{1}.txt'.
                             format(self.resultsCart['Symbol'],
                                    self.resultsCart['Date']), 'a')

class UpDnVolumeReport(CreateReportTxtFile):

    def updnVolReport(self):
        print()
        reportPivot = list(range(0,15))
        reportPivot[0] = ('Symbol: ', self.resultsCart['Symbol'].upper())
        reportPivot[1] = ('First Date: ', str(self.resultsCart['FirstDate']))
        reportPivot[2] = ('Last Date: ', str(self.resultsCart['Date']))
        reportPivot[3] = ('Days in Range: ', str(self.resultsCart['DaysUsed']))
        # reportPivot[4] = ('OnBalVolume First: ', str(self.resultsCart['OBVFirst']))
        # reportPivot[5] = ('OnBalVolume Last: ', str(self.resultsCart['OBVLast']))
        reportPivot[4] = ('OnBalVolume Change: ', str(self.resultsCart['OBVChange']))
        reportPivot[5] = ('Up Days: ', str(self.resultsCart['UpDaysCount']))
        reportPivot[6] = ('Up Volume Mean: ', str(self.resultsCart['UpVolumeMean']))
        reportPivot[7] = ('Down Days: ', str(self.resultsCart['DownDaysCount']))
        reportPivot[8] = ('Down Volume Mean: ', str(self.resultsCart['DownVolumeMean']))
        reportPivot[9] = ('Up:Down Days Ratio: ', str(self.resultsCart['UpDownDaysRatio']))
        reportPivot[10] = ('Up:Down Volume Ratio: ', str(self.resultsCart['UpDownVolumeRatio']))
        reportPivot[11] = ('First Price: ', str(self.resultsCart['FirstPrice']))
        reportPivot[12] = ('Last Price: ', str(self.resultsCart[''
                                                                'Price']))
        reportPivot[13] = ('Price Change: ', str(self.resultsCart['PriceChg']))
        reportPivot[14] = ('Percent Change: ', str(self.resultsCart['PctPriceChg']))

        self.fileWrite.writelines('\n')
        self.fileWrite.writelines('∞UP:DOWN VOLUME REPORT∞')
        self.fileWrite.writelines('\n')
        for i in range(15):
            print(reportPivot[i][0],reportPivot[i][1])
            self.fileWrite.writelines((reportPivot[i][0],reportPivot[i][1]))
            self.fileWrite.writelines('\n')
        self.fileWrite.close()

        print("{0} {1} Pivots Report for {2}".
              format(self.choice1,self.resultsCart['Date'],self.resultsCart['Symbol']))

class MovAvgVolumeReport(CreateReportTxtFile):

    def movAvgVolume(self):
            # fileWrite = open('reports/Rpt{0}{1}.txt'.format(self.resultsCart['Symbol'],
            #                                                 self.resultsCart['Last Date']), 'a')
            reportRange = list(range(0,5))
            reportRange[0] = ('Symbol: ', self.resultsCart['Symbol'].upper(), '\n')
            reportRange[1] = ('First Date: ', str(self.resultsCart['FirstDate']), '\n')
            reportRange[2] = ('Latest Date: ', str(self.resultsCart['Date']), '\n')
            reportRange[3] = ('Moving Avg Length (Days): ',str(self.resultsCart['MovingAvgLength']), '\n' )
            reportRange[4] = ('Moving Average: ',str(self.resultsCart['MovingAverage']), '\n')

            self.fileWrite.writelines('\n')
            self.fileWrite.writelines('∞MOVING AVERAGE REPORT∞')
            self.fileWrite.writelines('\n')
            for i in range(5):
                print(reportRange[i][0], reportRange[i][1])
                self.fileWrite.writelines((reportRange[i][0], reportRange[i][1]))
                self.fileWrite.writelines('\n')

            self.fileWrite.close()

            print("{0} {1} Ranges Report for {2}".
                  format(self.choice1, self.resultsCart['Date'], self.resultsCart['Symbol']))

class VOVVolumeReport(CreateReportTxtFile):

    def VOVVolume(self):
            # fileWrite = open('reports/Rpt{0}{1}.txt'.format(self.resultsCart['Symbol'],
            #                                                 self.resultsCart['Last Date']), 'a')
            reportRange = list(range(0,11))
            reportRange[0] = ('Symbol: ', self.resultsCart['Symbol'].upper(), '\n')
            reportRange[1] = ('Up Days Count: ', str(self.resultsCart['UpDaysCountVOV']), '\n')
            reportRange[2] = ('Up Days VOV Mean: ', str(self.resultsCart['UpVolumeVOVMean']), '\n')
            reportRange[3] = ('Down Days Count: ',str(self.resultsCart['DownDaysCountVOV']), '\n' )
            reportRange[4] = ("Down Days VOV Mean: ", str(self.resultsCart['DownVolumeVOVMean']), '\n')
            reportRange[5] = ("Up: Down Days Ratio: ", str(self.resultsCart['Up:DownVOVDaysRatio']), '\n')
            reportRange[6] = ("Up: Down VOV Mean Ratio: ", str(self.resultsCart['Up:DownVOVMeanRatio']), '\n')
            reportRange[7] = ("Fist Price: ", str(self.resultsCart['FirstPrice']), '\n')
            reportRange[8] = ("Last Price: ", str(self.resultsCart['LastPrice']), '\n')
            reportRange[9] = ("Price Change: ", str(self.resultsCart['PriceChange']), '\n')
            reportRange[10] = ("Percent Price Change: ", str(self.resultsCart['PctPriceChange']), '\n')

            self.fileWrite.writelines('\n')
            self.fileWrite.writelines('∞VOV REPORT∞')
            self.fileWrite.writelines('\n')
            for i in range(11):
                print(reportRange[i][0], reportRange[i][1])
                self.fileWrite.writelines((reportRange[i][0], reportRange[i][1]))
                self.fileWrite.writelines('\n')

            self.fileWrite.close()

            print("{0} {1} Ranges Report for {2}".
                  format(self.choice1, self.resultsCart['Date'], self.resultsCart['Symbol']))


def main(code, results):
    print()
    choice1 = input("Create New Report ('c') or Add to Existing Report ('a')? ")

    if code == 'UpDnVolume':
        b = UpDnVolumeReport()
        b.setParameters(choice1, results)
        b.updnVolReport()
    elif code == 'MovAvgVolume':
        b = MovAvgVolumeReport()
        b.setParameters(choice1,results)
        b.movAvgVolume()
    elif code == 'VOV':
        b = VOVVolumeReport()
        b.setParameters(choice1, results)
        b.VOVVolume()
    else:
        print("Invalid Code")

######################################################
######################################################

        # reportPivot = fileIn.readlines()
        # fileIn = open('PivotsRpt.txt','r')

        # timeStampToday = str(datetime.date.today())
        # fileWrite = open('reports/Rpt{0}{1}.txt'.format(self.resultsCart['Symbol'],
        #                     self.resultsCart['Date']), 'a')
        # reportPivot0 = ('Symbol: ', self.resultsCart['Symbol'], '\n')
        # reportPivot1 = ('Date: ', self.resultsCart['Date'], '\n')
        # reportPivot2 = ('Days Used: ', str(self.resultsCart['Days Used']), '\n')
        # reportPivot3 = ('Close: ', str(self.resultsCart['Close']), '\n')
        # reportPivot4 = ('Pivot Point: ', str(self.resultsCart['Pivot Point']), '\n')
        # reportPivot5 = ('Support1: ', str(self.resultsCart['Support1']), '\n')
        # reportPivot6 = ('Support2: ', str(self.resultsCart['Support2']), '\n')
        # reportPivot7 = ('Resistance1: ', str(self.resultsCart['Resistance1']), '\n')
        # reportPivot8 = ('Resistance2: ', str(self.resultsCart['Resistance2']), '\n')
        #
        # fileWrite.writelines('\n')
        # fileWrite.writelines(reportPivot0)
        # fileWrite.writelines(reportPivot1)
        # fileWrite.writelines(reportPivot2)
        # fileWrite.writelines(reportPivot3)
        # fileWrite.writelines(reportPivot4)
        # fileWrite.writelines(reportPivot5)
        # fileWrite.writelines(reportPivot6)
        # fileWrite.writelines(reportPivot7)
        # fileWrite.writelines(reportPivot8)


        # for k,v in self.resultsCart.items():
        #     # fileWrite.writelines(k,v)
        #     print('z: ', k,v)