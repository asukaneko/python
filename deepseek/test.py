import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 常量设置
G = 6.67430e-11  # 引力常数 (m³ kg⁻¹ s⁻²)
M_earth = 5.972e24  # 地球质量 (kg)
R_earth = 6371e3  # 地球半径 (m)
earth_rot_speed = 465.1  # 地球赤道自转线速度 (m/s)

# 导弹参数
dt = 0.1  # 时间步长 (秒)
total_time = 1800  # 总模拟时间 (秒)


def icbm_trajectory():
    # 初始条件：赤道发射，向东发射利用地球自转
    initial_altitude = 0  # 发射海拔 (m)
    launch_speed = 7e3  # 初始速度 (m/s)
    launch_angle = 45  # 发射角度 (度)

    # 初始位置 (地球表面)
    x0 = R_earth + initial_altitude
    y0 = 0
    z0 = 0

    # 初始速度分解（考虑地球自转）
    theta = np.radians(launch_angle)
    vx = 0
    vy = launch_speed * np.cos(theta) + earth_rot_speed
    vz = launch_speed * np.sin(theta)

    # 初始化状态数组
    positions = [[x0, y0, z0]]
    velocities = [[vx, vy, vz]]

    for t in np.arange(0, total_time, dt):
        x, y, z = positions[-1]
        vx, vy, vz = velocities[-1]

        # 计算到地心的距离
        r = np.sqrt(x ** 2 + y ** 2 + z ** 2)

        # 计算引力加速度
        a_grav = -G * M_earth / r ** 3
        ax = a_grav * x
        ay = a_grav * y
        az = a_grav * z

        # 欧拉法积分
        new_vx = vx + ax * dt
        new_vy = vy + ay * dt
        new_vz = vz + az * dt

        new_x = x + vx * dt
        new_y = y + vy * dt
        new_z = z + vz * dt

        # 检测碰撞地球
        if np.sqrt(new_x ** 2 + new_y ** 2 + new_z ** 2) <= R_earth:
            break

        positions.append([new_x, new_y, new_z])
        velocities.append([new_vx, new_vy, new_vz])

    return np.array(positions)


def plot_trajectory(positions):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制地球
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = R_earth * np.outer(np.cos(u), np.sin(v))
    y = R_earth * np.outer(np.sin(u), np.sin(v))
    z = R_earth * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='b', alpha=0.2)

    # 绘制轨迹
    x = positions[:, 0]
    y = positions[:, 1]
    z = positions[:, 2]
    ax.plot(x, y, z, label='Missile Trajectory', color='r')

    # 设置坐标轴
    max_range = np.max([np.abs(x), np.abs(y), np.abs(z)])
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_title('ICBM Trajectory Simulation')
    plt.legend()
    plt.show()


# 运行模拟并绘图
positions = icbm_trajectory()
plot_trajectory(positions)