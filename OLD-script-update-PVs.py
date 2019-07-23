import epics
import time

numbs = []
for i in range(1,101):
    numbs.append((i,i/50))

while True:
    itr = 1
    while itr < 100:
        v1,v2 = numbs[itr][0],numbs[itr][1]
        epics.caput("DIAG_MTCA09:PICO_CH4:AVG_RD",v1)
        epics.caput("DIAG_MTCA09:PICO_CH4:STD_RD",v2)    
        itr += 1
        print("avg:",v1,"std-dev:",v2)
        time.sleep(0.3)
