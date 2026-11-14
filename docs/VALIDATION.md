# 发布前验证记录

验证日期：2026-11-14。环境：Ubuntu 24.04.2、ROS 2 Jazzy、Python 3.12。
本仓库的验证与 FishBot 主项目独立进行。

## 已执行并通过

| 检查 | 结果 |
| --- | --- |
| 构建 | 2 个包通过，不依赖主项目工作空间 |
| colcon 回归测试 | 10 项，0 错误、0 失败、0 跳过 |
| 仓库完整性检查 | 3 项通过 |
| 线程练习 | 3 个工作线程输出回调结果，全部 join 后进程正常退出 |
| 离线发布订阅 | 通过实际 ROS 2 话题收到随包文本的全部 3 条不同消息 |
| Turtlesim 控制 | offscreen 模式从约 `(5.544, 5.544)` 行驶到约 `(1.088, 1.048)`，随后控制指令为零速度，位置误差约 0.100 米 |
| 依赖与网络 | 运行示例不发起在线小说下载，不需要 FishBot、Nav2 或 Gazebo |

控制回归包含正/负转向、跨 π 的最短角度、到点停车、速度限幅、非有限数值和无效控制参数；线程回归验证结果回调与工作线程回收。

## 复验入口

```bash
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
colcon test --event-handlers console_cohesion+
colcon test-result --verbose
python3 -m pytest -q tests
ros2 run demo_python_pkg learn_thread
ros2 launch demo_python_topic pubsub_demo.launch.py
```

另一个测试会话中运行：

```bash
ros2 launch demo_python_topic turtle_demo.launch.py target_x:=1.0 target_y:=1.0
```

无桌面时可在启动 Turtlesim 的终端设置 `QT_QPA_PLATFORM=offscreen`，再观察 `/turtle1/pose` 和 `/turtle1/cmd_vel`。
不要让圆周运动节点和目标点控制节点同时向同一只海龟发送控制命令。

## 局限

- 自动化测试没有验证桌面窗口的实际显示效果。
- 不是实体机器人运动控制包；未针对真实机器人动力学、障碍物避让或安全停车机制验证。
- GitHub CI 文件已提供，但不把本地测试结果写成云端 CI 成功记录。
