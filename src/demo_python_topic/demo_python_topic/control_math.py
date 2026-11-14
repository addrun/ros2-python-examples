# SPDX-License-Identifier: Apache-2.0
"""Pure proportional-control functions for the turtlesim exercise."""
import math

def normalize_angle(angle):
    return math.atan2(math.sin(angle), math.cos(angle))

def compute_velocity(x, y, theta, target_x, target_y,
                     gain=1.0, max_speed=3.0, max_turn_rate=2.0, tolerance=0.1):
    if not all(math.isfinite(v) for v in (x, y, theta, target_x, target_y,
                                          gain, max_speed, max_turn_rate, tolerance)):
        raise ValueError('Control values must be finite.')
    if min(gain, max_speed, max_turn_rate, tolerance) <= 0:
        raise ValueError('Control limits and tolerance must be positive.')
    distance = math.hypot(target_x - x, target_y - y)
    if distance <= tolerance:
        return 0.0, 0.0
    error = normalize_angle(math.atan2(target_y - y, target_x - x) - theta)
    turn = max(-max_turn_rate, min(max_turn_rate, gain * error))
    # Turn in the shortest signed direction before moving forward.
    linear = min(max_speed, gain * distance) if abs(error) <= 0.1 else 0.0
    return linear, turn
