import math
import os
import random
import re
import sys
n = 4
if n % 2 == 0 and n > 20 and 1 <= n <= 100:
    print("Not Weird")
elif n % 2 != 0 and 1 <= n <= 100:
    print("Weird")
elif 2 <= n >= 5 and 1 <= n <= 100:
    print("Not Weird")
elif 6 <= n >= 20 and 1 <= n <= 100:
    print("Weird")