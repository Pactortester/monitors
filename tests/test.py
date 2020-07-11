# -*- coding: utf-8 -*-
from monitors.monitor_util import monitor_start


def test_monitor():
    monitor_start(name='chrome.exe')