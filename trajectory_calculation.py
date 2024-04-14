import math
import matplotlib.pyplot as plt
import numpy as np

class UFO:
    def __init__(self, alpha, v_i, a, x_i, y_i):
        self.alpha = alpha*math.pi/180
        self.v_i = v_i
        self.a = a
        self.x_i = x_i
        self.y_i = y_i

    def __repr__(self) -> str:
        return f'Object that starts off with an initial velocity of {self.v_i} m/s, acceleration of {self.a} m/s^2 at an angle of {self.alpha}. Initial position {self.x_i},{self.y_i}'

def trajectory(x_i, y_i, v_i, a, alpha, delta_t):
    t = 0
    x_path = []
    y_path = []
    vy_evolution = []
    vx_i = v_i * math.cos(alpha)
    vy_i = v_i * math.sin(alpha)
    y = 0
    while y >= 0:
        y = y_i + vy_i * t + 0.5*a*t**2
        x = x_i + vx_i * t
        vy = vy_i + a * t
        x_path.append(x)
        y_path.append(y)
        vy_evolution.append(vy)
        t += delta_t
    return x_path, y_path, vy_evolution, t


t_increment = 0.01
test_1 = UFO(45, 10, -9.8, 0, 0)
x_evolution, y_evolution, vy_evolution, total_time_of_flight = trajectory(test_1.x_i, test_1.y_i, test_1.v_i, test_1.a, test_1.alpha, t_increment)

with open('report.txt', 'w') as report:
    report.write(f'The total amount of flight is: {round(total_time_of_flight,2)} seconds.\n')
    report.write(f'Maximum height reached: {round(max(y_evolution),2)} m.\n')
    report.write(f'It reached a distance of {round(max(x_evolution),2)} m before touching the ground.')

flight = [i for  i in np.arange(0, total_time_of_flight, t_increment)]
vy_evolution.append(test_1.v_i* math.sin(test_1.alpha)+test_1.a*total_time_of_flight)
y_evolution.append(test_1.v_i* math.sin(test_1.alpha)*total_time_of_flight+0.5*test_1.a*total_time_of_flight**2)
x_evolution.append(test_1.v_i* math.cos(test_1.alpha)*total_time_of_flight)

fig, (ax1, ax2, ax3) = plt.subplots(3,1)
ax1.set_xlabel('Distance (m)')
ax1.set_ylabel('Height (m)')
ax1.plot(x_evolution, y_evolution)

ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Height (m)')
ax2.plot(flight, y_evolution)

ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Speed (m/s)')
ax3.plot(flight, vy_evolution)

plt.savefig('trajectory_data.png')
plt.show()