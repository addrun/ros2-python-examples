# ROS 2 Python 配套学习示例

一个独立的 **ROS 2 Jazzy Python 基础练习仓库**：节点、日志、发布订阅、队列/线程与 Turtlesim 控制。
它是 [FishBot 导航巡检项目](https://github.com/addrun/ros2-fishbot-patrol) 的配套学习材料，**不是主项目的子目录、子模块或运行依赖**。

来源和许可见 [NOTICE.md](NOTICE.md)。所有文本示例离线运行，不下载小说、不分发教材 PDF。

## 构建

目标环境：Ubuntu 24.04、ROS 2 Jazzy；先安装 ROS 2、rosdep 和 colcon。

```bash
git clone https://github.com/addrun/ros2-python-examples.git
cd ros2-python-examples
source /opt/ros/jazzy/setup.bash
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro jazzy -r -y
colcon build --symlink-install
source install/setup.bash
```

每个新终端都需要 source ROS 2 和当前工作空间。该仓库不需要安装 FishBot、Nav2 或 Gazebo。

## 1. 最小节点与日志

```bash
ros2 run demo_python_pkg python_node
```

观察日志；`Ctrl+C` 退出。

## 2. 线程与结果回调

```bash
ros2 run demo_python_pkg learn_thread
```

三个工作线程分别计算本地示例文本的单词数，通过同一个回调打印结果，全部完成后退出。
这是 Python 并发辅助示例，不是 ROS 2 执行器并发机制的替代。

## 3. 话题发布、订阅、队列和工作线程

```bash
ros2 launch demo_python_topic pubsub_demo.launch.py
```

发布端从随包安装的 `data/demo_lines.txt` 读取原创示例句子，每秒向 `/novel` 发布一条消息。
订阅回调将消息放入有界队列，后台线程处理并打印，展示消息接收与耗时任务解耦的结构。
历史可执行文件名 `novel_pub_node` / `novel_sub_node` 保留；这里不实现音频朗读。

分终端运行或传入自己的 UTF-8 文本：

```bash
# 终端 1
ros2 run demo_python_topic novel_sub_node
# 终端 2
ros2 run demo_python_topic novel_pub_node --ros-args       -p text_file:=/absolute/path/to/sample.txt -p period:=0.5 -p repeat:=false
# 终端 3
ros2 topic echo /novel
```

## 4. Turtlesim 目标点控制

```bash
ros2 launch demo_python_topic turtle_demo.launch.py target_x:=1.0 target_y:=1.0
```

控制器订阅 `/turtle1/pose` 并发布 `/turtle1/cmd_vel`。
使用归一化后的有符号角度误差，先转向再前进；到达容差范围后发布零速度。
`gain`、`max_speed`、`max_turn_rate`、`tolerance` 可通过 ROS 参数覆盖。

圆周运动示例需要另外启动 Turtlesim，并避免同时运行目标点控制器：

```bash
# 终端 1
ros2 run turtlesim turtlesim_node
# 终端 2
ros2 run demo_python_topic turtle_circle
```

## 测试

```bash
colcon test --event-handlers console_cohesion+
colcon test-result --verbose
python3 -m pytest -q tests
```

回归用例覆盖左右转方向、跨 π 的角度归一化、到点停车、速度限幅和异常参数。
实际验证范围见 [docs/VALIDATION.md](docs/VALIDATION.md)。
无桌面时可用 `QT_QPA_PLATFORM=offscreen` 运行 Turtlesim 进行消息级测试，但看不到交互窗口。

## 目录

```text
src/
  demo_python_pkg/       节点、日志、离线线程练习
  demo_python_topic/     发布订阅、随包文本、Turtlesim、回归测试
tests/                   仓库完整性检查
docs/VALIDATION.md        验证记录与局限
```

## 许可

Apache-2.0，保留原功能包许可证。本仓库是学习练习集，不是实体机器人控制方案。
