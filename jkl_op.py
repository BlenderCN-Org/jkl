import bpy

class JKL_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.jkl_controls"
    bl_label = "jkl Controls"
    bl_description = "jkl Controls"
    
    mode = bpy.props.StringProperty()
    
    def execute(self, context):
        scr = bpy.context.screen
        scops = bpy.ops.screen
        sce = bpy.context.scene
        
        print(self.mode)
        print(bpy.context.scene.frame_current)
        
        if self.mode == "j":
            if scr.is_animation_playing == True:
                scops.animation_play()
                scops.animation_play(reverse=True)
            else:
                scops.animation_play(reverse=True)
        elif self.mode == "l":
            if scr.is_animation_playing == True:
                scops.animation_play()
                scops.animation_play()
            else:
                scops.animation_play()
        elif self.mode == "kj":
            if scr.is_animation_playing == True:
                scops.animation_play()
            sce.frame_set(sce.frame_current - 1)
        elif self.mode == "kl":
            if scr.is_animation_playing == True:
                scops.animation_play()
            sce.frame_set(sce.frame_current + 1)
        else:
            if scr.is_animation_playing == True:
                scops.animation_play()
                
        return {'FINISHED'}