import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv("Results/csv_bin/csv_2/PCHIP_2/script_2_pchip_data_position.csv")
data2 = pd.read_csv("Results/csv_bin/csv_2/PCHIP_2/script_2_pchip_data_smoothposition.csv")
data3 = pd.read_csv("Results/csv_bin/csv_2/PCHIP_2/script_2_pchip_data_velocity.csv")
data4 = pd.read_csv("Results/csv_bin/csv_2/PCHIP_2/script_2_pchip_data_acceleration.csv")

## Q POSITION, VELOCITY, ACCELERATION [Joint 1 - 3] ##
plt.subplot(3, 3, 1)
plt.subplots_adjust(hspace = 0.4)
plt.title("q1-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["Q_Position_1"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Position (rad)")
#---------#
plt.subplot(3, 3, 2)
plt.title("q2-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["Q_Position_2"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Position (rad)")
#---------#
plt.subplot(3, 3, 3)
plt.title("q3-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["Q_Position_3"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Position (rad)")
#---------#
#---------#
plt.subplot(3, 3, 4)
plt.title("v1-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["Velocity_1"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Velocity (rad/s)")
#---------#
plt.subplot(3, 3, 5)
plt.title("v2-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["Velocity_2"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Velocity (rad/s)")
#---------#
plt.subplot(3, 3, 6)
plt.title("v3-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["Velocity_3"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Velocity (rad/s)")
#---------#
#---------#
plt.subplot(3, 3, 7)
plt.title("a1-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Acceleration_1"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Acceleration (rad/s)")
#---------#
plt.subplot(3, 3, 8)
plt.title("a2-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Acceleration_2"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Acceleration (rad/s)")
#---------#
plt.subplot(3, 3, 9)
plt.title("a3-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Acceleration_3"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Acceleration (rad/s)")
plt.show()


## Q POSITION, VELOCITY, ACCELERATION [Joint 4 - 6] ##
plt.subplot(3, 3, 1)
plt.subplots_adjust(hspace = 0.4)
plt.title("q4-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["Q_Position_4"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Position (rad)")
#---------#
plt.subplot(3, 3, 2)
plt.title("q5-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["Q_Position_5"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Position (rad)")
#---------#
plt.subplot(3, 3, 3)
plt.title("q6-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["Q_Position_6"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Position (rad)")
#---------#
#---------#
plt.subplot(3, 3, 4)
plt.title("v4-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["Velocity_4"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Velocity (rad/s)")
#---------#
plt.subplot(3, 3, 5)
plt.title("v5-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["Velocity_5"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Velocity (rad/s)")
#---------#
plt.subplot(3, 3, 6)
plt.title("v6-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["Velocity_6"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Velocity (rad/s)")
#---------#
#---------#
plt.subplot(3, 3, 7)
plt.title("a4-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Acceleration_4"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Acceleration (rad/s)")
#---------#
plt.subplot(3, 3, 8)
plt.title("a5-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Acceleration_5"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Acceleration (rad/s)")
#---------#
plt.subplot(3, 3, 9)
plt.title("a6-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Acceleration_6"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Acceleration (rad/s)")
plt.show()


## Q POSITION [Grippers] ##
plt.subplot(1, 2, 1)
plt.title("g1-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["Gripper_1"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Position (rad)")
#---------#
plt.subplot(1, 2, 2)
plt.title("g2-t; Trajectory 2 [PCHIP]")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["Gripper_2"])
plt.xlabel("Time (s)")
plt.ylabel("Joint Position (rad)")
plt.show()