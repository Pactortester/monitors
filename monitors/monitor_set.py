# -*- coding: utf-8 -*-

"""
Parameter initialization is a global variable by default. When calling the relevant API,
you need to inherit the setting class and set the corresponding parameters.

"""


class Settings(object):

    # Windows specific settings, default ‘explorer.exe'
    # If the program you want to monitor is started by app A, write A here
    process_parent_name = 'explorer.exe'

    monitor_log_path = 'monitor_log'
    refresh_interval = 3
    monitor_duration = 1
