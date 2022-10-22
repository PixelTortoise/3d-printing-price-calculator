from numpy import dstack


import sys

configs = []

try:
    configTxt = open('config.txt', 'r')
    configsraw = configTxt.readlines()
    configTxt.close()
except:
    print('Config txt not found! Generating it now...')

    try:
        configTxt = open('config.txt', 'w')
        configTxt.write('maintainenceBill = 0.50\nmarkup = 2\nroundUp = true\nprintReceipt = true')
        configTxt.close()
        print('Config txt generated successfully! Make sure you change the settings to your liking, after you press enter to close the program of course.')
        cont = input()
        sys.exit() 

    except:
        ('Some error occurred when making the config txt, either this is your garbage pc, or my garbage code, probobly the latter, but in either case try it again, maybe it will actually work. Press enter to close the program.')
        cont = input()
        sys.exit()

for i in configsraw:
    configs.append(i.replace('\n', ''))

try:
    maintainenceBill = float(configs[0].replace('maintainenceBill = ', ''))

    markup = float(configs[1].replace('markup = ', ''))

    roundUp = configs[2].replace('roundUp = ', '')
    if roundUp == 'true':
        roundUp = True
    elif roundUp == 'false':
        roundUp = False
    
    printReceipt = configs[3].replace('printReceipt = ', '')
    if printReceipt == 'true':
        printReceipt = True
    elif printReceipt == 'false':
        printReceipt = False

except:
    'An error occured, double check the config txt syntax, press enter to close the program.'
    cont = input()
    sys.exit()