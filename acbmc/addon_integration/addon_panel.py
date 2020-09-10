import bpy

class AddonPanel(bpy.types.Panel):
    bl_idname = "spinu2b_py_runner_addon_panel"
    bl_label = "spinu2b_py_runner_addon_panel_label"
    bl_category = "Python Scripts Runner"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("view3d.run_python_script", text="Run Python script")