#!/usr/bin/env python
# coding: utf-8

# # Analyze Ball on Incline data
# Use this notebook to quickly test whether your ball on incline data makes sense!

# In[4]:


# Imports
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import math


# ## Reading the data
# 
# The function "read_csv(filename)" takes in a filename and returns numpy arrays with time and voltage.

# In[5]:


def read_csv(filename):
    """Read CSV from Waveforms"""
    dat = np.genfromtxt(filename, delimiter=',', skip_header=13, names=True)
    time = dat['Time_s']
    voltage = dat['Channel_1_V']
    return time, voltage

def find_midpoints(time, voltage, show_plot=True):
    """Find timing of ball crossings"""
    # Write a function yourself, which identifies the peaks in the voltage,
    # and returns values for passing times and (possibly) their uncertainties
    # in it (but they are generally very small!).
    t_pass = []
    t_pass_sigma = [0.0001, 0.00001]
    t_end = []
    for i in range(len(time)):
        if voltage[i]>3.5 and voltage[i]-voltage[i-1]>0.25:
            t_pass.append(time[i])

    for i in range(len(time)):
        if voltage[i]-voltage[i-1]<0.25 and voltage[i]>3.5 and voltage[i+1]<3.5:
            t_end.append(time[i])

    return t_pass, t_end, t_pass_sigma


# In[6]:


# Read the data and plot it (possibly with passing times in):
ball1_try1 = 'data/ball1_try1.csv'
ball1_try2 = 'data/ball1_try2.csv'
ball1_try3 = 'data/ball1_try3.csv'

ball2_try1 = 'data/ball2_try1.csv'
ball2_try2 = 'data/ball2_try2.csv'
ball2_try3 = 'data/ball2_try3.csv'

ball3_try1 = 'data/ball3_try1.csv'
ball3_try2 = 'data/ball3_try2.csv'
ball3_try3 = 'data/ball3_try3.csv'

flip_ball1_try1 = 'data/ball1_try1_flipped.csv'
flip_ball1_try2 = 'data/ball1_try2_flipped.csv'
flip_ball1_try3 = 'data/ball1_try3_flipped.csv'

flip_ball2_try1 = 'data/ball2_try1_flipped.csv'
flip_ball2_try2 = 'data/ball2_try2_flipped.csv'
flip_ball2_try3 = 'data/ball2_try3_flipped.csv'

flip_ball3_try1 = 'data/ball3_try1_flipped.csv'
flip_ball3_try2 = 'data/ball3_try2_flipped.csv'
flip_ball3_try3 = 'data/ball3_try3_flipped.csv'

times_ball1_try1 = []
times_ball1_try2 = []
times_ball1_try3 = []

times_ball2_try1 = []
times_ball2_try2 = []
times_ball2_try3 = []

times_ball3_try1 = []
times_ball3_try2 = []
times_ball3_try3 = []

times_ball1_end1 = []
times_ball1_end2 = []
times_ball1_end3 = []

times_ball2_end1 = []
times_ball2_end2 = []
times_ball2_end3 = []

times_ball3_end1 = []
times_ball3_end2 = []
times_ball3_end3 = []


for i in [1,2,3]:
    for j in [1,2,3]:
        time, voltage = read_csv('data/ball' + str(i) + '_try' + str(j) + '.csv')
        timepass, timeend, timepass_sig = find_midpoints(time, voltage)
        #'balltry' + str(i)+str(j) == timepass
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(time, voltage, label='Measurements')
        ax.vlines(x = timepass, ymin = 0, ymax = 5, color = "green")
        ax.vlines(x = timeend, ymin = 0, ymax = 5, color = "orange")
        ax.set_title("Ball" + str(i) + "Try " + str(j))
        ax.set_xlabel("Time (s)", fontsize=18)
        ax.set_ylabel("Voltage (V)", fontsize=18)
        print("for ball " + str(i) + "try " + str(j) +  str(timepass))
        if i == 1 and j ==1:
            times_ball1_try1 = timepass
            times_ball1_end1 = timeend
        if i == 1 and j ==2:
            times_ball1_try2 = timepass
            times_ball1_end2 = timeend
        if i == 1 and j ==3:
            times_ball1_try3 = timepass
            times_ball1_end3 = timeend

        if i == 2 and j ==1:
            times_ball2_try1 = timepass
            times_ball2_end1 = timeend
        if i == 2 and j ==2:
            times_ball2_try2 = timepass
            times_ball2_end2 = timeend
        if i == 2 and j ==3:
            times_ball2_try3 = timepass
            times_ball2_end3 = timeend

        if i == 3 and j ==1:
            times_ball3_try1 = timepass
            times_ball3_end1 = timeend
        if i == 3 and j ==2:
            times_ball3_try2 = timepass
            times_ball3_end2 = timeend
        if i == 3 and j ==3:
            times_ball3_try3 = timepass
            times_ball3_end3 = timeend

for i in [1,2,3]:
    for j in [1,2,3]:
        time, voltage = read_csv('data/ball' + str(i) + '_try' + str(j) + '_flipped.csv')
        timepass, timeend, timepass_sig = find_midpoints(time, voltage)
        'flippedballtry' + str(i)+str(j) == timepass
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(time, voltage, label='Measurements')
        ax.vlines(x = timepass, ymin = 0, ymax = 5, color = "black")
        ax.vlines(x = timeend, ymin = 0, ymax = 5, color = "orange")
        ax.set_title("Flipped Setup Ball" + str(i) + "Try " + str(j))
        ax.set_xlabel("Time (s)", fontsize=18)
        ax.set_ylabel("Voltage (V)", fontsize=18)
        print("for ball flipped " + str(i) + "try " + str(j) +  str(timepass))
        if i == 1 and j ==1:
            flip_times_ball1_try1 = timepass
            flip_times_ball1_end1 = timeend
        if i == 1 and j ==2:
            flip_times_ball1_try2 = timepass
            flip_times_ball1_end2 = timeend
        if i == 1 and j ==3:
            flip_times_ball1_try3 = timepass
            flip_times_ball1_end3 = timeend

        if i == 2 and j ==1:
            flip_times_ball2_try1 = timepass
            flip_times_ball2_end1 = timeend
        if i == 2 and j ==2:
            flip_times_ball2_try2 = timepass
            flip_times_ball2_end2 = timeend
        if i == 2 and j ==3:
            flip_times_ball2_try3 = timepass
            flip_times_ball2_end3 = timeend

        if i == 3 and j ==1:
            flip_times_ball3_try1 = timepass
            flip_times_ball1_end1 = timeend
        if i == 3 and j ==2:
            flip_times_ball3_try2 = timepass
            flip_times_ball3_end2 = timeend
        if i == 3 and j ==3:
            flip_times_ball3_try3 = timepass
            flip_times_ball3_end3 = timeend


# # What to do next?
# 
# From the V(t) data you should be able to determine five times at which the ball passed. Discuss in the group how to do this best, and possibly test it by seeing if the result is "invariant" between different data sets.
# 
# Note that getting an uncertainty can be hard, and think about the relevance of such an uncertainty, which should anyway be rather small.

# In[7]:


def get_times(times):
    times_new = times
    timings = []
    for i in range(0, len(times_new)-1):
        if np.abs(times_new[i]-times_new[i+1]) >= 0.05:
            timings.append(times_new[i])
    timings.append(times_new[len(times_new)-1])
    #timings = timings - timings[0]
    return timings



# In[8]:


time_ball1_trz1 = get_times(times_ball1_try1)
print(time_ball1_trz1)

time_ball1_end1 = get_times(times_ball1_end1)
print(time_ball1_end1)

time_ball1_trz2 = get_times(times_ball1_try2)
print(time_ball1_trz2)

time_ball1_end2 = get_times(times_ball1_end2)
print(time_ball1_end2)


time_ball1_trz3 = get_times(times_ball1_try3)
print(time_ball1_trz3)

time_ball1_end3 = get_times(times_ball1_end3)
print(time_ball1_end3)

time_ball2_try1 = get_times(times_ball2_try1)
print(time_ball2_try1)
time_ball2_try2 = get_times(times_ball2_try2)
print(time_ball2_try2)
time_ball2_try3 = get_times(times_ball2_try3)
print(time_ball2_try3)

time_ball2_end1 = get_times(times_ball2_end1)
print(time_ball2_end1)
time_ball2_end2 = get_times(times_ball2_end2)
print(time_ball2_end2)
time_ball2_end3 = get_times(times_ball2_end3)
print(time_ball2_try3)

time_ball3_try1 = get_times(times_ball3_try1)
print(time_ball3_try1)

time_ball3_end1 = get_times(times_ball3_end1)
print(time_ball3_end1)

time_ball3_try2 = get_times(times_ball3_try2)
print(time_ball3_try2)

time_ball3_end2 = get_times(times_ball3_end2)
print(time_ball3_end2)

time_ball3_try3 = get_times(times_ball3_try3)
print(time_ball3_try3)

time_ball3_end3 = get_times(times_ball3_end3)
print(time_ball3_end3)


# In[ ]:


def find_true_middle(start, end):
    middle = np.zeros_like(start)
    for i in range(len(start)):
        middle[i] = start[i] + 0.5*(end[i]-start[i])
    return middle

middle_ball1_try1 = find_true_middle(time_ball1_trz1, time_ball1_end1)
print(middle_ball1_try1)

middle_ball1_try2 = find_true_middle(time_ball1_trz2, time_ball1_end2)
print(middle_ball1_try2)

middle_ball1_try3 = find_true_middle(time_ball1_trz3, time_ball1_end3)
print(middle_ball1_try3)

middle_ball2_try1 = find_true_middle(time_ball2_try1, time_ball2_end1)
print(middle_ball2_try1)

middle_ball2_try2 = find_true_middle(time_ball2_try2, time_ball2_end2)
print(middle_ball2_try2)

middle_ball2_try3 = find_true_middle(time_ball2_try3, time_ball2_end3)
print(middle_ball2_try3)

middle_ball3_try1 = find_true_middle(time_ball3_try1, time_ball3_end1)
print(middle_ball3_try1)

middle_ball3_try2 = find_true_middle(time_ball3_try2, time_ball3_end2)
print(middle_ball3_try2)

middle_ball3_try3 = find_true_middle(time_ball3_try3, time_ball3_end3)
print(middle_ball3_try3)



# In[10]:


#other data

#position of the gates

s_gates = [80.95, 65.15, 50.30, 35.05, 20.15]
mc_gates = [80.8, 65.15, 50.35, 35.05, 20.15]
mg_gates = [81.5, 65.33, 50.45, 35.25, 20.3]

s_gates = np.flip(s_gates)
mc_gates = np.flip(mc_gates)
mg_gates = np.flip(mg_gates)

average_gate = np.zeros_like(s_gates)

for i in range(0,5):
    average_gate[i] = (s_gates[i] + mc_gates[i] + mg_gates[i])/3

def calc_distance_gate(measurements):
    distances = []
    for i in range(0,4):
        d = measurements[i+1] - measurements[i] 
        distances.append(d)
    return distances

distances_s = calc_distance_gate(s_gates)
distances_mc = calc_distance_gate(mc_gates)
distances_mg = calc_distance_gate(mg_gates)

distances_average = np.zeros_like(distances_s)
for i in range(0,4):
    distances_average[i] = (distances_s[i] + distances_mc[i] + distances_mg[i])/3

print(distances_average)
#angles

angle_table = 90.1

goni_mg1 = 14
goni_mc1 = 14
goni_s1 = 14

goni_mg2 = 13.9
goni_mc2 = 13.9
goni_s2 = 13.9

#trigonometry in cm

op_mg = 22.2
op_mc = 21.8
op_s = 22.15

op_err = 0.05

ad_mg = 89.75
ad_mc = 89.1
ad_s = 89.75

ad_err = 0.05

def trig_error(a,b, deltaa, deltab):
    error = math.degrees(abs(1 / b / (a ** 2 / b ** 2 + 1)) * deltaa + abs(-(a / b ** 2 / (a ** 2 / b ** 2 + 1))) * deltab)
    return error

trig_mg =math.degrees(np.arctan((op_mg/ad_mg)))
trig_mg_err = trig_error(op_mg, ad_mg, op_err, ad_err)
print(trig_mg)
print(trig_mg_err)
trig_mc =math.degrees(np.arctan((op_mc/ad_mc)))
trig_mc_err = trig_error(op_mc, ad_mc, op_err, ad_err)
print(trig_mc)
print(trig_mc_err)
trig_s =math.degrees(np.arctan((op_s/ad_s)))
trig_s_err = trig_error(op_s, ad_s, op_err, ad_err)
print(trig_s)
print(trig_s_err)

trig_ave = (trig_mc + trig_mg + trig_s)/3
trig_ave_err = (trig_mc_err + trig_mg_err + trig_s_err)/3
print("the average angle from trigonometry is " + str(trig_ave) + "with an error of " + str(trig_ave_err) + ".")

#diameter of balls in mm

diameter_s = 10, 15, 19
diameter_mc = 9.9, 14.9, 18.9
diameter_mg = 10, 15, 19

err_diamter = 0.1
#railwidth in mm
railwidthsara = 6
railwidthmc = 6
railwidthmg = 6

error_rail = 0.5


# In[11]:


def calc_a(distances, time):
    acceleration = []
    for i in range(0,4):
        a = 0.4
        acceleration.append(a)
    return acceleration

calc_a(distances_average, middle_ball1_try1)


# In[12]:


def calc_g(a, theta, D_ball, d_rail):
    g = (a)/np.sin(theta)*(1 + 2/5 + (D_ball**2)/(D_ball**2 - d_rail**2))
    return g


# In[13]:


def calc_error_g(a, theta, D_ball, d_rail, delt_a, delta_theta, delta_D_ball, delta_d_rail):
    delta_g = delt_a *1/np.sin(theta)*(1 + 2/5 + (D_ball**2)/(D_ball**2 - d_rail**2))#..
    return delta_g


# In[ ]:


combined = np.block([[middle_ball1_try1], [middle_ball1_try2], [middle_ball1_try3], [middle_ball2_try1], [middle_ball2_try2], [middle_ball2_try3], [middle_ball3_try1], [middle_ball3_try2], [middle_ball3_try3]])
print(combined)


# In[ ]:




