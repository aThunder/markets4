import datetime

class CreateReportTxtFile():
    # def __init__(self,choice1,results):

    def setParameters(self, choice1, results):
        self.resultsCart = results

        if choice1 == 'c':
            self.choice1 = 'Created '
            self.fileWrite = open('reports/Rpt{0}RANGES{1}.txt'.
                             format(self.resultsCart['Symbol'],
                             self.resultsCart['Date']), 'w')
        elif choice1 == 'a':
            self.choice1 = 'Updated '
            self.fileWrite = open('reports/Rpt{0}RANGES{1}.txt'.
                             format(self.resultsCart['Symbol'],
                                    self.resultsCart['Date']), 'a')

class PivotsReport(CreateReportTxtFile):

    def pivots(self):
        print()
        reportPivot = list(range(0,9))
        reportPivot[0] = ('Symbol: ', self.resultsCart['Symbol'].upper())
        reportPivot[1] = ('Date: ', self.resultsCart['Date'])
        reportPivot[2] = ('Base Days: ', str(self.resultsCart['Days Used']))
        reportPivot[3] = ('Close: ', str(self.resultsCart['Close']))
        reportPivot[4] = ('Pivot Point: ', str(self.resultsCart['Pivot Point']))
        reportPivot[5] = ('Support1: ', str(self.resultsCart['Support1']))
        reportPivot[6] = ('Support2: ', str(self.resultsCart['Support2']))
        reportPivot[7] = ('Resistance1: ', str(self.resultsCart['Resistance1']))
        reportPivot[8] = ('Resistance2: ', str(self.resultsCart['Resistance2']))

        self.fileWrite.writelines('\n')
        self.fileWrite.writelines('∞PIVOTS REPORT∞')
        self.fileWrite.writelines('\n')
        for i in range(9):
            print(reportPivot[i][0],reportPivot[i][1])
            self.fileWrite.writelines((reportPivot[i][0],reportPivot[i][1]))
            self.fileWrite.writelines('\n')
        self.fileWrite.close()

        print("{0} {1} Pivots Report for {2}".
              format(self.choice1,self.resultsCart['Date'],self.resultsCart['Symbol']))

class RangesReport(CreateReportTxtFile):

    def ranges(self):
            # fileWrite = open('reports/Rpt{0}{1}.txt'.format(self.resultsCart['Symbol'],
            #                                                 self.resultsCart['Last Date']), 'a')
            reportRange = list(range(0,20))
            reportRange[0] = ('Symbol: ', self.resultsCart['Symbol'].upper(), '\n')
            reportRange[1] = ('First Date: ', str(self.resultsCart['First Date']), '\n')
            reportRange[2] = ('Latest Date: ', str(self.resultsCart['Date']), '\n')
            reportRange[3] = ('Range Length (Days): ',str(self.resultsCart['Range Length']), '\n' )
            reportRange[4] = ('First Close: ',str(self.resultsCart['First Close']), '\n')
            reportRange[5] = ('Latest Close: ', str(self.resultsCart['Latest Close']), '\n')
            reportRange[6] = ('Range Price Chg: ', str(self.resultsCart['Range Price Change']), '\n')
            reportRange[7] = ('Percent Price Chg: ', str(self.resultsCart['Pct Change']), '\n')
            reportRange[8] = ('Range High: ', str(self.resultsCart['Range High']), '\n')
            reportRange[9] = ('Range Low: ', str(self.resultsCart['Range Low']), '\n')
            reportRange[10] = ('Range Closing High: ', str(self.resultsCart['Range Closing High']), '\n')
            reportRange[11] = ('Range Closing Low: ', str(self.resultsCart['Range Closing Low']), '\n')
            reportRange[12] = ('Range High Date: ', str(self.resultsCart['Range High Date']), '\n')
            reportRange[13] = ('Range Low Date: ', str(self.resultsCart['Range Low Date']), '\n')
            reportRange[14] = ('Range Closing High Date: ', str(self.resultsCart['Range Closing High Date']), '\n')
            reportRange[15] = ('Range Closing Low Date: ', str(self.resultsCart['Range Closing Low Date']), '\n')
            reportRange[16] = ('High/Low Range: ', str(self.resultsCart['High/Low Range']), '\n')
            reportRange[17] = ('High Close/Low Close Range: ', str(self.resultsCart['High Close/Low Close Range']), '\n')
            reportRange[18] = ('Latest Close in Overall Range: ', str(self.resultsCart['Current Close in Overall Range']), '\n')
            reportRange[19] = ('Latest Close in Overall Closing Range: ', str(self.resultsCart['Current Close in Overall Closing Range']), '\n')


            self.fileWrite.writelines('\n')
            self.fileWrite.writelines('∞RANGES REPORT∞')
            self.fileWrite.writelines('\n')
            for i in range(20):
                print(reportRange[i][0], reportRange[i][1])
                self.fileWrite.writelines((reportRange[i][0], reportRange[i][1]))
                self.fileWrite.writelines('\n')

            self.fileWrite.close()

            print("{0} {1} Ranges Report for {2}".
                  format(self.choice1, self.resultsCart['Date'], self.resultsCart['Symbol']))

def main(code,results):
    print()
    choice1 = input("Create New Report ('c') or Add to Existing Report ('a')? ")

    if code == 'pivots':
        b = PivotsReport()
        b.setParameters(choice1, results)
        b.pivots()
    elif code == 'ranges':
        b = RangesReport()
        b.setParameters(choice1,results)
        b.ranges()
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