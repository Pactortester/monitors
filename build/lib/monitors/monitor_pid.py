# -*- coding: utf-8 -*-
import platform

import psutil
from monitors.monitor_set import Settings as ST


def get_process_id(process_name):
    """
    获取应用主进程pid
    :return:
    """

    if platform.system() == 'Windows':
        process_parent_name = ST.process_parent_name
        app_pid = []
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if p.name() == process_name:
                app_pid.append(pid)

        app_parent_pid = []
        for app in app_pid:
            p = psutil.Process(app)
            if p.parent().name() == process_parent_name:
                app_parent_pid.append(app)
        return app_parent_pid[0]

    else:
        app_pid = []
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if p.name() == process_name:
                app_pid.append(pid)
        return app_pid[0]
