# SPDX-License-Identifier: Apache-2.0
import math
import pytest
from demo_python_topic.control_math import compute_velocity, normalize_angle

def test_turns_clockwise_when_target_is_below():
    linear, angular = compute_velocity(0, 0, 0, 0, -1)
    assert linear == 0
    assert angular < 0

def test_turns_counterclockwise_when_target_is_above():
    assert compute_velocity(0, 0, 0, 0, 1)[1] > 0

def test_shortest_angle_wraps_at_pi():
    assert normalize_angle(2 * math.pi - 0.2) == pytest.approx(-0.2)

def test_stops_at_target():
    assert compute_velocity(1, 1, 2, 1, 1) == (0.0, 0.0)

def test_speed_is_capped():
    assert compute_velocity(0, 0, 0, 100, 0)[0] == 3.0

@pytest.mark.parametrize('bad', [float('nan'), float('inf')])
def test_rejects_nonfinite_input(bad):
    with pytest.raises(ValueError):
        compute_velocity(0, 0, 0, bad, 0)

def test_rejects_invalid_limits():
    with pytest.raises(ValueError):
        compute_velocity(0, 0, 0, 1, 0, max_speed=-1)
