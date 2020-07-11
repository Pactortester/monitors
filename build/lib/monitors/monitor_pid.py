# -*- coding: utf-8 -*-
import platform

import psutil


def get_process_id(process_name):
    """
    获取应用主进程pid
    :return:
    """
    process_parent_name = None
    if platform.system() == 'Windows':
        process_parent_name = 'explorer.exe'
    # TODO linux and mac parent name
    elif platform.system() == 'Linux':
        process_parent_name = '*'

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
