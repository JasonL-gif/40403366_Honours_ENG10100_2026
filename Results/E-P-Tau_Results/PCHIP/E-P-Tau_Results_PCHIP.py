import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv("Results/csv_bin/csv_1/PCHIP_1/script_1_pchip_data_energy_power.csv")
data2 = pd.read_csv("Results/csv_bin/csv_2/PCHIP_2/script_2_pchip_data_energy_power.csv")
data3 = pd.read_csv("Results/csv_bin/csv_3/PCHIP_3/script_3_pchip_data_energy_power.csv")

data4 = pd.read_csv("Results/csv_bin/csv_1/PCHIP_1/script_1_pchip_data_torque.csv")
data5 = pd.read_csv("Results/csv_bin/csv_2/PCHIP_2/script_2_pchip_data_torque.csv")
data6 = pd.read_csv("Results/csv_bin/csv_3/PCHIP_3/script_3_pchip_data_torque.csv")

## ENERGY ##
plt.subplot(1, 3, 1)
plt.title("E-t; Trajectory 1")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["Energy"])
plt.xlabel("Time (s)")
plt.ylabel("Energy Consumption/cycle (J)")
plt.ylim(0, 90)
#---------#
plt.subplot(1, 3, 2)
plt.title("E-t; Trajectory 2")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color=  (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["Energy"])
plt.xlabel("Time (s)")
plt.ylabel("Energy Consumption/cycle (J)")
plt.ylim(0, 90)
#---------#
plt.subplot(1, 3, 3)
plt.title("E-t; Trajectory 3")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["Energy"])
plt.xlabel("Time (s)")
plt.ylabel("Energy Consumption/cycle (J)")
plt.ylim(0, 90)
plt.show()

## POWER ##
plt.subplot(1, 3, 1)
plt.title("P-t; Trajectory 1")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data1["Time"], data1["Power"])
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.ylim(0, 23)
#---------#
plt.subplot(1, 3, 2)
plt.title("P-t; Trajectory 2")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data2["Time"], data2["Power"])
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.ylim(0, 23)
#---------#
plt.subplot(1, 3, 3)
plt.title("P-t; Trajectory 3")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data3["Time"], data3["Power"])
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.ylim(0, 23)
plt.show()

## TORQUE ##
plt.subplot(2, 3, 1)
plt.title("Tau_1-t; Traj 1")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Torque_1"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 5)
#---------#
plt.subplot(2, 3, 2)
plt.title("Tau_1-t; Traj 2")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data5["Time"], data5["Torque_1"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 5)
#---------#
plt.subplot(2, 3, 3)
plt.title("Tau_1-t; Traj 3")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data6["Time"], data6["Torque_1"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 5)
#---------#
plt.subplot(2, 3, 4)
plt.title("Tau_2-t; Traj 1")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Torque_2"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 14)
#---------#
plt.subplot(2, 3, 5)
plt.title("Tau_2-t; Traj 2")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data5["Time"], data5["Torque_2"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 14)
#---------#
plt.subplot(2, 3, 6)
plt.title("Tau_2-t; Traj 3")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data6["Time"], data6["Torque_2"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 14)
plt.show()
#---------#
#---------#
plt.subplot(2, 3, 1)
plt.title("Tau_3-t; Traj 1")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Torque_3"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 15)
#---------#
plt.subplot(2, 3, 2)
plt.title("Tau_3-t; Traj 2")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data5["Time"], data5["Torque_3"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 15)
#---------#
plt.subplot(2, 3, 3)
plt.title("Tau_3-t; Traj 3")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data6["Time"], data6["Torque_3"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 15)
#---------#
plt.subplot(2, 3, 4)
plt.title("Tau_4-t; Traj 1")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Torque_4"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 1)
#---------#
plt.subplot(2, 3, 5)
plt.title("Tau_4-t; Traj 2")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data5["Time"], data5["Torque_4"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 1)
#---------#
plt.subplot(2, 3, 6)
plt.title("Tau_4-t; Traj 3")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data6["Time"], data6["Torque_4"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 1)
plt.show()
#---------#
#---------#
plt.subplot(2, 3, 1)
plt.title("Tau_5-t; Traj 1")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Torque_5"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 2)
#---------#
plt.subplot(2, 3, 2)
plt.title("Tau_5-t; Traj 2")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data5["Time"], data5["Torque_5"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 2)
#---------#
plt.subplot(2, 3, 3)
plt.title("Tau_5-t; Traj 3")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data6["Time"], data6["Torque_5"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 2)
#---------#
plt.subplot(2, 3, 4)
plt.title("Tau_6-t; Traj 1")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data4["Time"], data4["Torque_6"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 0.1)
#---------#
plt.subplot(2, 3, 5)
plt.title("Tau_6-t; Traj 2")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data5["Time"], data5["Torque_6"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 0.1)
#---------#
plt.subplot(2, 3, 6)
plt.title("Tau_6-t; Traj 3")         # Title of plot.
plt.grid() 
plt.axhline(0, 0, 1, color = (0, 0, 0, 1))      # Produces a horizontal line at q = 0.
plt.plot(data6["Time"], data6["Torque_6"])
plt.xlabel("Time (s)")
plt.ylabel("Actuator Torque (Nm)")
plt.ylim(0, 0.1)
plt.show()

