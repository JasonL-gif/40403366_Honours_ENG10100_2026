import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv("Final_Results/csv_4/script_4_data_box.csv")

# BOX TRAJECTORY AND PE; TRAJECTORY 4 ##
plt.subplot(2, 2, 1)
plt.title("x_box-t; Trajectory 4")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["x_Position"])
plt.xlabel("Time (s)")
plt.ylabel("x position (m)")
#---------#
plt.subplot(2, 2, 2)
plt.title("y_box-t; Trajectory 4")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["y_Position"])
plt.xlabel("Time (s)")
plt.ylabel("y position (m)")
#---------#
plt.subplot(2, 2, 3)
plt.title("z_box-t; Trajectory 4")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["z_Position"])
plt.xlabel("Time (s)")
plt.ylabel("z position (m)")
#---------#
plt.subplot(2, 2, 4)
plt.title("x-y; Trajectory 4")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["x_Position"], data1["y_Position"])
plt.xlabel("x Position (m)")
plt.ylabel("y position (m)")
plt.show()
#---------#
plt.title("Box Potential Energy; Trajectory 4")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))
plt.plot(data1["Time"], data1["PE_Box"])
plt.xlabel("Time (s)")
plt.ylabel("PE (J)")
plt.show()

