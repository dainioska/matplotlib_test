import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import numpy as np

style.use('ggplot')

CSV_HEADER = "Time,    Current,    Voltage"
CSV_FILE = "logs/powerTest"+str(datetime.date(2020, 12, 2))+".csv"

x = np.array([datetime.datetime(2020, 9, 28, i, 0)for i in range(12)])
y = np.random.randint(100, size=x.shape)


np.savetxt(CSV_FILE, x, delimiter=',', fmt="%s", header=CSV_HEADER)

print(x)
print(y)

plt.plot(x, y)
plt.show()