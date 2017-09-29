import math
import numpy as np

roll = 2.6335
pitch = 0.4506
yaw = 1.1684

print "roll = ", roll
print "pitch = ", pitch
print "yaw = ", yaw
print ""

yawMatrix = np.matrix([
[math.cos(yaw), -math.sin(yaw), 0],
[math.sin(yaw), math.cos(yaw), 0],
[0, 0, 1]
])

pitchMatrix = np.matrix([
[math.cos(pitch), 0, math.sin(pitch)],
[0, 1, 0],
[-math.sin(pitch), 0, math.cos(pitch)]
])

rollMatrix = np.matrix([
[1, 0, 0],
[0, math.cos(roll), -math.sin(roll)],
[0, math.sin(roll), math.cos(roll)]
])

R = yawMatrix * pitchMatrix * rollMatrix

theta = math.acos(((R[0, 0] + R[1, 1] + R[2, 2]) - 1) / 2)
multi = 1 / (2 * math.sin(theta))

rx = multi * (R[2, 1] - R[1, 2]) * theta
ry = multi * (R[0, 2] - R[2, 0]) * theta
rz = multi * (R[1, 0] - R[0, 1]) * theta

print rx, ry, rz
