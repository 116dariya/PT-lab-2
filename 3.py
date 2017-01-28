s = input()
import math
x = math.ceil(len(s) / 2)
print(s[x:] + s[:x])