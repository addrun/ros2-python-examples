# SPDX-License-Identifier: Apache-2.0
import ast
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

def test_only_companion_packages():
    names = {ET.parse(p).getroot().findtext('name') for p in (ROOT / 'src').glob('*/package.xml')}
    assert names == {'demo_python_pkg', 'demo_python_topic'}

def test_no_online_fetching():
    for path in (ROOT / 'src').rglob('*.py'):
        text = path.read_text()
        ast.parse(text, filename=str(path))
        assert 'requests.get(' not in text
        assert 'bie5.cc' not in text

def test_sample_data_is_nonempty():
    path = ROOT / 'src/demo_python_topic/data/demo_lines.txt'
    assert len([line for line in path.read_text().splitlines() if line.strip()]) >= 3
