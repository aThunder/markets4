# ControlStkListing.py

'''
    1. Prompts user to select category
    2. Calls the Control file for selected category
'''
import ControlStkVolumeB4a
import ControlStkRangeB4a
import ControlStk

class AllCategories():
    def __init__(self):
        filler = 1

    def promptForCategory(self):
        print()
        print("1. Stock Volume Indicators")
        print("2. Stock Range Indicators")
        print("3. Update Database")
        print("4. Exit")
        print()
        try:
            choice1 = int(input("Enter Choice: "))
            return choice1
        except:
            choice1 = "NOT AN INT"
            return choice1

    def callControlStkVolume(self):
        print("1. Stock Volume Indicators")
        ControlStkVolumeB4a.main()
    def callControlStkRange(self):
        print("2. Stock Range Indicators")
        ControlStkRangeB4a.main()
    def callControlStkUpdate(self):
        print("3. Update Database")
        ControlStk.main()

def main():
    a = AllCategories()
    b = a.promptForCategory()
    print()
    if b == 1:
        a.callControlStkVolume()
    elif b == 2:
        a.callControlStkRange()
    elif b == 3:
        a.callControlStkUpdate()
    elif b == 4:
        print("Exiting Program...Done")
    else:
        print()
        print("INCORRECT ENTRY")
        print("ENTER ONLY '1','2','3' OR '4'")
        print()
        print("TRY AGAIN")
        print()
        main()

    # print("EXITING PROGRAM")
if __name__ == '__main__': main()



################################
################################


