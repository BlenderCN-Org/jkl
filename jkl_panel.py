import bpy

class JKL_PT_Panel(bpy.types.Panel):
    bl_idname = "JKL_PT_Panel"
    bl_label = "JKL Panel"
    bl_category = "JKL Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align=True)
        row.operator('view3d.jkl_controls', text="", icon='BACK').mode = "kj"
        row.operator('view3d.jkl_controls', text="", icon='PLAY_REVERSE').mode = "j"
        row.operator('view3d.jkl_controls', text="", icon='PAUSE').mode = "k"
        row.operator('view3d.jkl_controls', text="", icon='PLAY').mode = "l"
        row.operator('view3d.jkl_controls', text="", icon='FORWARD').mode = "kl"
        
