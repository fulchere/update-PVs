import epics
import time
import numpy as np

numbs = []
for i in range(1,101):
    # List of 100 values ranging (1->100, 0->2)
    numbs.append((i,i/50))

while True:
    itr = 1
    while itr < 100:
        #v1,v2 = numbs[itr][0],numbs[itr][1]
        v1 = 50 + itr*0.3 + np.random.randn()*7
        v2 = 1 + np.random.randn()*0.1
        epics.caput("DIAG_MTCA09:PICO_CH4:AVG_RD",v1)
        epics.caput("DIAG_MTCA09:PICO_CH4:STD_RD",v2)  
        itr += 1
        print("avg:",v1,"std-dev:",v2)
        time.sleep(0.3)
