import bpy

# Add-on description
bl_info = {
    "name": "Sculpt Falloff Cycler",
    "description": "Cycles the falloff of sculpt brush",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sculpt > Sculpt Falloff Cycler",
    "warning": "",
    "wiki_url": "",
    "category": "Sculpt"
}

def sculpt_falloff_cycler(context):
    # Get the current falloff mode
    falloff_mode = context.tool_settings.sculpt.brush.curve_preset
    
    # Determine the next falloff mode in the cycle
    if falloff_mode == 'SMOOTH':
        new_falloff_mode = 'SPHERE'
    elif falloff_mode == 'SPHERE':
        new_falloff_mode = 'ROOT'
    elif falloff_mode == 'ROOT':
        new_falloff_mode = 'SHARP'
    elif falloff_mode == 'SHARP':
        new_falloff_mode = 'LIN'
    else:
        # Default to smooth falloff if the current mode is not recognized
        new_falloff_mode = 'SMOOTH'
    
    # Set the new falloff mode
    context.tool_settings.sculpt.brush.curve_preset = new_falloff_mode
    
    print("did curve_preset")


import bpy

class SculptFalloffCycler(bpy.types.Operator):
    """Cycles the sculpt brush falloff mode"""
    bl_idname = "sculpt.sculpt_falloff_cycler"
    bl_label = "Sculpt Falloff Cycler"

    def execute(self, context):
        # Do the curve preset
        sculpt_falloff_cycler(context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SculptFalloffCycler)
    
    # Add a keyboard shortcut for the operator
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Sculpt", space_type="EMPTY")
        kmi = km.keymap_items.new(SculptFalloffCycler.bl_idname, "F", "PRESS", alt=True)

def unregister():
    bpy.utils.unregister_class(SculptFalloffCycler)

