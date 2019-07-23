import epics
import time

while True:
    # All gets printed on one line
    print('%.3f'%epics.caget("ACS_DIAG:AVERAGE"),end=' ')
    print("is the average of",end=' ')
    v = epics.caget("ACS_DIAG:BSM_D2500:AVG_WIRE")
    print("[",'%.3f %.3f %.3f %.3f %.3f %.3f'%(v[0],v[1],v[2],v[3],v[4],v[5]),end=' ] ')
    print("the current wire value is",end=' ')
    print('%.3f'%epics.caget("ACS_DIAG:BSM_D2500:WIRE_RES"))

    # Delay
    time.sleep(0.1)
