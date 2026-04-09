import numpy as np
import mujoco as mj
import mujoco.viewer
import time
from Interpolation_1 import t_smooth, t_interp, q1_linear, q2_linear, q3_linear, q4_linear, q5_linear, q6_linear, gripper1_linear, gripper2_linear
from Trajectory_1_Gen import keyframe
import matplotlib.pyplot as plt
import pandas as pd

m = mujoco.MjModel.from_xml_path("../40403366_Honours_ENG10100_2026-main/trossen_vx300s/scene.xml")
d = mujoco.MjData(m)

sim_time = 20
dt = m.opt.timestep
total_energy = 0
time_elapsed = []
torque_traj = []
pow_traj = []
energy_traj = []
x_traj = []
y_traj = []
z_traj = []
PE_box_traj = []       

q1_acc_traj = []
q2_acc_traj = []
q3_acc_traj = []
q4_acc_traj = []
q5_acc_traj = []
q6_acc_traj = []

v1_traj = []
v2_traj = []
v3_traj = []
v4_traj = []
v5_traj = []
v6_traj = []

tau_1_traj = []
tau_2_traj = []
tau_3_traj = []
tau_4_traj = []
tau_5_traj = []
tau_6_traj = []

mujoco.mj_resetDataKeyframe(m, d, 0)

with mujoco.viewer.launch_passive(m, d) as viewer:              # With the MuJoCo software launched as required, with the model, data. (Launched as viewer [i.e. mujoco.viewer])
        while viewer.is_running() and d.time < sim_time:        # While the simulation is running, and the time of the simulation is less than the max. time of the simulation
                viewer.cam.azimuth = 180        # Sets camera in front of robot                       
                viewer.cam.elevation = -40      # Angles camera 
                time_start = time.time()        ####
                d.ctrl[0] = q1_linear(d.time)   # Each of these lines sets an interpolated path from "Interpolation_1" to an actuator, allowing it 
                                                # to move in accordance with the q-t graph.
                d.ctrl[1] = q2_linear(d.time)
                d.ctrl[2] = q3_linear(d.time)
                d.ctrl[3] = q4_linear(d.time)
                d.ctrl[4] = q5_linear(d.time)
                d.ctrl[5] = q6_linear(d.time)
                d.ctrl[6] = gripper1_linear(d.time)
                mujoco.mj_step(m, d)            # Establishes a time-step within the situation, essentially telling the simulation to begin with the aforementioned conditions
                time_elapsed.append(d.time)     # Appends the time elapsed to an empty list
                print(d.time)
        # Trajectory Path
                pos = d.xpos[11]                # Position of the payload (box)
                x_pos = pos[0]                  # x-Position of the payload
                y_pos = pos[1]                  # y-Position of the payload
                z_pos = pos[2]                  # z-Position of the payload
                x_traj.append(x_pos)            # Appends x-co-ordinates during time to empty list
                y_traj.append(y_pos)            # Appends y-co-ordinates during time to empty list
                z_traj.append(z_pos)            # Appends z-co-ordinates during time to empty list
        # Velocity (Generalised)
                v1_traj.append(d.qvel[0])       # Appends the generalised velocity of each actuator to its respective empty list
                v2_traj.append(d.qvel[1])
                v3_traj.append(d.qvel[2])
                v4_traj.append(d.qvel[3])
                v5_traj.append(d.qvel[4])
                v6_traj.append(d.qvel[5])
        # Acceleration (Generalised)  
                q1_acc_traj.append(d.qacc[0])   # Appends the generalised acceleration of each actuator to its respective empty list
                q2_acc_traj.append(d.qacc[1])
                q3_acc_traj.append(d.qacc[2])
                q4_acc_traj.append(d.qacc[3])
                q5_acc_traj.append(d.qacc[4])
                q6_acc_traj.append(d.qacc[5])
        # Torque
                torque = d.qfrc_actuator        # Torque of the actuators.
                tau_1_traj.append(abs(torque[0]))    # Appends the actuator torque of each actuator to its respective empty list
                tau_2_traj.append(abs(torque[1]))
                tau_3_traj.append(abs(torque[2]))
                tau_4_traj.append(abs(torque[3]))
                tau_5_traj.append(abs(torque[4]))
                tau_6_traj.append(abs(torque[5]))
        # Power
                mech_pow = np.sum(np.abs(torque[0:7] * d.qvel[0:7]))    # Sum of mechanical power = Sum of (torque * velocty). Magnitude is considered, so the absolute value is used.
                pow_traj.append(mech_pow)       # Appends mechanical power to empty list
        # Total Energy Consumption
                total_energy += mech_pow * dt   # Energy consumption = the integral of mechanical power w.r.t time
                energy_traj.append(total_energy)        # Appends energy consumpoion to empty list
                torque_traj.append(np.sum(np.abs(torque)))      ######  
        # Potential Energy of Box
                PE_box = 0.25 * 9.81 * z_pos     # PE = mass of box * gravitational constant * height (z-co-ordinate) of the box
                PE_box_traj.append(PE_box)      # Appends PE of box to empty list
                viewer.sync()   # Syncs the simulation to the simulation viewer, so that each timestep can be viewed in sequence. Allows for the animation of the trajectory.

if __name__ == "__main__":
        max_PE = max(PE_box_traj)
        max_power = max(pow_traj)
        print("--- Energy Consumption ---")
        print(f"{total_energy:.3f} J")
        print("--- Max PE ---")
        print(f"{max_PE:.3f} J")
        print("--- Final Torque ---")
        print(f"{torque_traj[-1]:.3f} Nm")
        print("---Max Power---")
        print(f"{max_power:.3f} W")

        # csv Data
        data_1 = {"Time": time_elapsed,
                  "Energy": energy_traj,
                  "Power": pow_traj,
                  }
        
        data_2 = {"Time": time_elapsed,
                  "Torque_1": tau_1_traj,
                  "Torque_2": tau_2_traj,
                  "Torque_3": tau_3_traj,
                  "Torque_4": tau_4_traj,
                  "Torque_5": tau_5_traj,
                  "Torque_6": tau_6_traj,
                  }
        
        data_3 = {"Time": time_elapsed,
                  "x_Position": x_traj,
                  "y_Position": y_traj,
                  "z_Position": z_traj,
                  "PE_Box": PE_box_traj}
        
        data_4 = {"Time": t_interp,
                  "Q_Position_1": q1_linear(t_interp),
                  "Q_Position_2": q2_linear(t_interp),
                  "Q_Position_3": q3_linear(t_interp),
                  "Q_Position_4": q4_linear(t_interp),
                  "Q_Position_5": q5_linear(t_interp),
                  "Q_Position_6": q6_linear(t_interp),
                  "Gripper_1": gripper1_linear(t_interp),
                  "Gripper_2": gripper2_linear(t_interp)
                  }
        
        data_5 = {"Time": time_elapsed,
                  "Velocity_1": v1_traj,
                  "Velocity_2": v2_traj,
                  "Velocity_3": v3_traj,
                  "Velocity_4": v4_traj,
                  "Velocity_5": v5_traj,
                  "Velocity_6": v6_traj,
                  }
        
        data_6 = {"Time": time_elapsed,
                  "Acceleration_1": q1_acc_traj,
                  "Acceleration_2": q2_acc_traj,
                  "Acceleration_3": q3_acc_traj,
                  "Acceleration_4": q4_acc_traj,
                  "Acceleration_5": q5_acc_traj,
                  "Acceleration_6": q6_acc_traj
                  }

        dataframe1 = pd.DataFrame(data_1)
        dataframe2 = pd.DataFrame(data_2)
        dataframe3 = pd.DataFrame(data_3)
        dataframe4 = pd.DataFrame(data_4)
        dataframe5 = pd.DataFrame(data_5)
        dataframe6 = pd.DataFrame(data_6)

        dataframe1.to_csv("Results/csv_bin/csv_1/script_1_data_energy_power.csv")
        dataframe2.to_csv("Results/csv_bin/csv_1/script_1_data_torque.csv")
        dataframe3.to_csv("Results/csv_bin/csv_1/script_1_data_box.csv")
        dataframe4.to_csv("Results/csv_bin/csv_1/script_1_data_position.csv")
        dataframe5.to_csv("Results/csv_bin/csv_1/script_1_data_velocity.csv")
        dataframe6.to_csv("Results/csv_bin/csv_1/script_1_data_acceleration.csv")
