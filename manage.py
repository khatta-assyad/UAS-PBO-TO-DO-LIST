#!/usr/bin/env python
import os
import sys
import importlib.util

folder_name = "todo-list"
module_name = "settings"
settings_path = os.path.join(os.path.dirname(__file__), folder_name, "settings.py")

spec = importlib.util.spec_from_file_location("todolist.settings", settings_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

os.environ["DJANGO_SETTINGS_MODULE"] = "todolist.settings"

from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
