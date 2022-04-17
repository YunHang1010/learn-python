import time,subprocess

# timeLeft = 60
# while timeLeft > 0:
#     print(timeLeft,end='')
#     time.sleep(1)
#     timeLeft = timeLeft -1
    
# subprocess.Popen(['open','alarm.wav'])

timeLeft = 10
while timeLeft > 0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

fileObj = open('/Users/sunyunhang/Desktop/countdown.txt','w')
fileObj.write('Break time is over!')
fileObj.close()
subprocess.Popen(['open','/Users/sunyunhang/Desktop/countdown.txt'])