import bpy

from acbmc.runner import BlenderAddonLogicRunner
from acbmc.scene_setups.bone_world_matrices.runners \
    .simple_case_mat_calc_verif_run import SimpleCaseMatricesCalculationVerificationRunner



class RunPythonScriptOperator(bpy.types.Operator):
    bl_idname = "view3d.run_python_script"
    bl_label = "Simple operator"
    bl_description = "Run Python script"

    runner_blender_script = SimpleCaseMatricesCalculationVerificationRunner

    def execute(self, context):
        self.runner_blender_script().execute()
        return {'FINISHED'}