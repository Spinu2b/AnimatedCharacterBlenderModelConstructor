import bpy
from acbmc.scene_setups \
    .bone_world_matrices_calculation_verification_runner \
     import BoneWorldMatricesCalculationVerificationRunner

from acbmc.runner import BlenderAddonLogicRunner


class RunPythonScriptOperator(bpy.types.Operator):
    bl_idname = "view3d.run_python_script"
    bl_label = "Simple operator"
    bl_description = "Run Python script"

    runner_blender_script = BoneWorldMatricesCalculationVerificationRunner

    def execute(self, context):
        self.runner_blender_script().execute()
        return {'FINISHED'}