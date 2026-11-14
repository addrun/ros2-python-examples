# SPDX-License-Identifier: Apache-2.0
from demo_python_pkg.learn_thread import count_words, main

def test_worker_uses_result_callback():
    results = []
    count_words('sample', 'ROS 2 nodes', lambda name, count: results.append((name, count)))
    assert results == [('sample', 3)]

def test_demo_joins_workers(capsys):
    main()
    output = capsys.readouterr().out
    assert len(output.strip().splitlines()) == 3
