import numpy as np 

x = [3,5,6,7,8]
y = [3,4,6,9,8]

x = np.array(x)
y = np.array(y)

result = x^y
print(result)

for i in range(len(x)):
    if result[i] == 0:
        print("index number  : ",i ,end="")
        print("element : ",x[i])
