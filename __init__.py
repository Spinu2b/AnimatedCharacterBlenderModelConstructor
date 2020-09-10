
bl_info = {
    "name": "Python scripts runner for debug capabilities with Blender Development extension for VSCode",
    "author": "Spinu2b",
    "description": "This addon is supposed to act as a runner for Python scripts for convenient debugging using Blender Development extension for Visual Studio Code",
    "blender": (2, 90, 0),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.absolute()))


import bpy
from acbmc.addon_integration.run_python_script_op import RunPythonScriptOperator
from acbmc.addon_integration.addon_panel import AddonPanel

classes = (RunPythonScriptOperator, AddonPanel)

register, unregister = bpy.utils.register_classes_factory(classes)
