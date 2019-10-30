areaTotal = 0
looping = True
minusLooping = False
while looping == True:
    try:
        height = int(input('Enter the height of the wall in m: '))
        width = int(input('Enter the width of the wall in m: '))
        area = height * width
        areaTotal += area
        done = input('Is this your final input? (Y/N)')
        if done == 'Y' or done == 'y':
            looping = False
            minusLooping = True
        elif done == 'N' or done == 'n':
            print('Continuing...')
        else:
            print('Continuing...')
    except ValueError:
        print('Invalid input - please enter again.')
while minusLooping == True:
    try:
        minusHeight = int(input('Enter the height of the area in m: '))
        minusWidth = int(input('Enter the width of the area in m: '))
        minusArea = minusHeight * minusWidth
        areaTotal -= minusArea
        minusDone = input('Is this your final input? (Y/N)')
        if minusDone == 'Y' or minusDone == 'y':
            minusLooping = False
            final = 1 + areaTotal // 11
            print('The amount of paint needed to paint the room is '+str(final)+' litres.')
        elif minusDone == 'N' or minusDone == 'n':
            print('Continuing...')
        else:
            print('Continuing...')
    except ValueError:
        print('Invalid input - please enter again.')