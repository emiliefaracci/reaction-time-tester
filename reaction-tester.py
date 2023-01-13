
import time
import random 

print("press enter when prompted 'click now!' to see your reaction time in milliseconds\n")
print ("3")
time.sleep(1)
print ("2")
time.sleep(1)
print ("1...\n")
time.sleep(1)

list = []

i = 0
while i<30:
    waittime = random.randint(1,3)
    time.sleep(waittime)
    print("click now!")
    stime = time.time()
    inputhere = input()
    etime = time.time()
    reactiontime = str(round((etime - stime) * 1000))
    list.append(reactiontime)
    print(reactiontime)
    i+=1

time.sleep(1)
print("\n\nresult recorded:")
print(*list, sep = ", ")
exit()
