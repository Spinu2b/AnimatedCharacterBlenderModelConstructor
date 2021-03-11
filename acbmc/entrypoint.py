import pathlib
import sys

from mathutils import Quaternion
sys.path.append(str(pathlib.Path(__file__).parent.parent.absolute()))

from acbmc.blender_operations.blender_scene_manipulator import BlenderSceneManipulator
from acbmc.blender_operations.model_build.max_builtin_blend_fbx_exp_comp_anim_char_const import \
 MaxBuiltinBlenderFbxExportComplianceAnimatedCharacterConstructor
from acbmc.model.animated_character.constructing.animated_character_description_loader \
    import AnimatedCharacterDescriptionLoader, AnimatedCharacterDescriptionLoaderForTesting
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription

from acbmc.model.animated_character.model.math.vector3d import Vector3d


class SpaceTransformations:
    @staticmethod
    def position3d_transformation(vector3d: Vector3d):
        vector3d.y, vector3d.z = vector3d.z, vector3d.y

    @staticmethod
    def rotation_transformation(quaternion: Quaternion):
        quaternion.y, quaternion.z = quaternion.z, quaternion.y


class ImportAnimatedCharacterLogic:
    def execute(self, filepath_to_import: str):
        animated_character_description = AnimatedCharacterDescriptionLoaderForTesting().load(filepath_to_import)  # type: AnimatedCharacterDescription
        # BlenderSceneManipulator().clear_scene()
        animated_character_description.reform_space_model(
            position3d_transformation=SpaceTransformations.position3d_transformation,
            rotation_transformation=SpaceTransformations.rotation_transformation
        )
        animated_character_constructor = MaxBuiltinBlenderFbxExportComplianceAnimatedCharacterConstructor()
        animated_character_constructor.construct_animated_character(animated_character_description)


if __name__ == '__main__':
    ImportAnimatedCharacterLogic().execute()
