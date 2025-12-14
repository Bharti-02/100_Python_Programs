#replace all number greater than 15 with 0

import numpy as np
arr=np.array([5, 10, 15, 20, 25, 30])
arr[arr>15]=0
print(arr)