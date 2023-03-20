import matplotlib.pyplot as plt
import numpy as np
 

a = ['Male', 'Female']
b1 = np.array([279, 200])
b2 = np.array([81, 156])
b3 = np.array([132, 160])
b4 = np.array([492, 516])
 

plt.bar(a, b1, color='r')
plt.bar(a, b2, bottom=b1, color='b')
plt.bar(a, b3, bottom=b1+b2, color='y')
plt.bar(a, b4, bottom=b1+b2+b3, color='g')
plt.xlabel("Gender")
plt.ylabel("Number of people watching")
plt.legend(["Game", "Commercials", "won't watch", "Total"])
plt.title("Stack bar graph")
plt.show()