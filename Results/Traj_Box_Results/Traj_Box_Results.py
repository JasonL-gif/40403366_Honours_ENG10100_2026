import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv("Results/csv_bin/csv_1/script_1_data_box.csv")  # Extracts all data pertaining to the box from .csv file
data2 = pd.read_csv("Results/csv_bin/csv_2/script_2_data_box.csv")
data3 = pd.read_csv("Results/csv_bin/csv_3/script_3_data_box.csv")

## BOX TRAJECTORY AND PE; TRAJECTORY 1 ##
plt.subplot(2, 2, 1)  # Produces several plots in one page
plt.title("x_box-t; Trajectory 1")  # Title    
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["x_Position"])  # Plots time in the x-axis, and x position in the y - axis
plt.xlabel("Time (s)")  # Labels
plt.ylabel("x position (m)")
#---------#
plt.subplot(2, 2, 2)
plt.title("y_box-t; Trajectory 1")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["y_Position"])
plt.xlabel("Time (s)")
plt.ylabel("y position (m)")
#---------#
plt.subplot(2, 2, 3)
plt.title("z_box-t; Trajectory 1")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["z_Position"])
plt.xlabel("Time (s)")
plt.ylabel("z position (m)")
#---------#
plt.subplot(2, 2, 4)
plt.title("x-y; Trajectory 1")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["x_Position"], data1["y_Position"])
plt.xlabel("x Position (m)")
plt.ylabel("y position (m)")
plt.show()
#---------#
plt.title("Box Potential Energy; Trajectory 1")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))
plt.plot(data1["Time"], data1["PE_Box"])
plt.xlabel("Time (s)")
plt.ylabel("PE (J)")
plt.show()

## BOX TRAJECTORY AND PE; TRAJECTORY 2 ##
plt.subplot(2, 2, 1)
plt.title("x_box-t; Trajectory 2")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["x_Position"])
plt.xlabel("Time (s)")
plt.ylabel("x position (m)")
#---------#
plt.subplot(2, 2, 2)
plt.title("y_box-t; Trajectory 2")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["y_Position"])
plt.xlabel("Time (s)")
plt.ylabel("y position (m)")
#---------#
plt.subplot(2, 2, 3)
plt.title("z_box-t; Trajectory 2")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["z_Position"])
plt.xlabel("Time (s)")
plt.ylabel("z position (m)")
#---------#
plt.subplot(2, 2, 4)
plt.title("x-y; Trajectory 2")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["x_Position"], data2["y_Position"])
plt.xlabel("x Position (m)")
plt.ylabel("y position (m)")
plt.show()
#---------#
plt.title("Box Potential Energy; Trajectory 2")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))
plt.plot(data2["Time"], data2["PE_Box"])
plt.xlabel("Time (s)")
plt.ylabel("PE (J)")
plt.show()

## BOX TRAJECTORY AND PE; TRAJECTORY 3 ##
plt.subplot(2, 2, 1)
plt.title("x_box-t; Trajectory 3")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["x_Position"])
plt.xlabel("Time (s)")
plt.ylabel("x position (m)")
#---------#
plt.subplot(2, 2, 2)
plt.title("y_box-t; Trajectory 3")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["y_Position"])
plt.xlabel("Time (s)")
plt.ylabel("y position (m)")
#---------#
plt.subplot(2, 2, 3)
plt.title("z_box-t; Trajectory 3")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["z_Position"])
plt.xlabel("Time (s)")
plt.ylabel("z position (m)")
#---------#
plt.subplot(2, 2, 4)
plt.title("x-y; Trajectory 3")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["x_Position"], data3["y_Position"])
plt.xlabel("x Position (m)")
plt.ylabel("y position (m)")
plt.show()
#---------#
plt.title("Box Potential Energy; Trajectory 3")
plt.grid()
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))
plt.plot(data3["Time"], data3["PE_Box"])
plt.xlabel("Time (s)")
plt.ylabel("PE (J)")
plt.show()

## 3D PLOTS ##
