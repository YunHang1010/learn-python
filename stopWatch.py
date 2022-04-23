import time


print('Press RNTER to begin.Afterwards,press ENTER to "click" the stopwatch. Press the Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input('\n')
        lapTime = round(time.time() - lastTime,1)
        totalTime = round(time.time() - startTime,1)
        print('Lap #%s: %s  %s' % (lapNum,totalTime,lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')