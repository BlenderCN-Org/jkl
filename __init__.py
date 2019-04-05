bl_info = {
    "name" : "jkl_addon",
    "author" : "Dan Pool (dpdp)",
    "description" : "JKL Addon",
    "blender" : (2, 80, 0),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . jkl_op import JKL_OT_Operator
from . jkl_panel import JKL_PT_Panel

classes = (JKL_OT_Operator, JKL_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)