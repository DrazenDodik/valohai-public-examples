import debugpy
import numpy as np
import time
 
debugpy.listen(5678)
 
# The script is halted here, until a debugger is attached
debugpy.wait_for_client()
 
for x in range(1,20) :
    print(f"Doing computation {x}")
    data = np.random.random((50,50))
    sum = np.sum(data)
    time.sleep(2)