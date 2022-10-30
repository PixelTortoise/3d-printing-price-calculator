import sys
import os
import yaml
import math

filChoices = []
loopFil = True

try: # attemps to load yaml
    with open('config.yaml', 'r') as file: 
        config = yaml.safe_load(file)

except: # if it cannot it generates one
    config_yaml = '''
    maintainenceFee: 0.50
    markup: 2
    printReceipt: False
    roundUp: False
    '''

    config = yaml.safe_load(config_yaml)

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)

    print('Config.yaml created! Please press enter to close the program and change it to your liking.')
    cont = input()
    sys.exit()

LorC = input('Would you like to load a filament config, or would you like to create a filament config? ("l" or "c" respectively)\n')

if LorC == 'l': # loading filconfig
    print('\nLoading filament config, what config would you like to use? Just start typing the name and it will narrow it down.\n')

    while loopFil == True: # start filament config scelector

        filChoices = [] # clearing list in case of restart

        for i in os.listdir(): # adds all filconfigs to a list
            if i.endswith('.yaml') and i != 'config.yaml':
                filChoices.append(i)

        for i in filChoices:
                print(i)

        while len(filChoices) > 1: 

            choice = input('\n')

            for i in filChoices: # takes all choices that do not start with the search and removes them
                if i.startswith(choice) == False:
                    filChoices.remove(i)

            if len(filChoices) > 1:
                for i in filChoices:
                    print(i)

        use = input('\nWould you like to use {} as your filament config? (y or n) '.format(filChoices[0]))

        print('\n')

        if use == 'y':
            loopFil = False

        elif use == 'n':
            loopFil = True

    with open(filChoices[0], 'r') as file: # reads scelected filconfig yaml
        filConfig = yaml.safe_load(file)

    filWeight = float(filConfig.get('weight'))
    filPrice = float(filConfig.get('price'))

    printWeight = float(input('How much filament does the print take? '))
    clientName = str(input('What is your clients name? '))
    clientProduct = str(input('What did they need? '))

    rawPrintPrice = filPrice/filWeight * printWeight

    printPrice = (rawPrintPrice * config.get('markup')) + rawPrintPrice + config.get('maintainenceFee')

    if config.get('roundUp') == True:
        printPrice = math.ceil(printPrice)

    elif config.get('roundUp') == False:
        printPrice = round(printPrice, 2)

    billtxt = open('{}bill.txt'.format(clientName), 'w')

    billtxt.write('{}s bill\nproduct: {}\nweight: {}\nfilament: {}\nprice: {}'.format(clientName, clientProduct, printWeight, filChoices[0].replace('Config.yaml', ''), printPrice))
    print('Txt generated!')

if LorC == 'c': # creating filconfig
    filName = input('\nCreating filament config, what is the name of the filament?\n')
    filWeight = input('\nWhat was the initial weight of the filament? (grams)\n')
    filPrice = input('\nWhat is the price of the spool?\n')
    
    # puts desired configurations into a yaml type format
    filConfig = ''' 
    weight: {}
    price: {}
    '''.format(filWeight, filPrice)

    filFile = yaml.safe_load(filConfig)

    with open('{}Config.yaml'.format(filName), 'w') as file: # writes filconfig
        yaml.dump(filFile, file)
