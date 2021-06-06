import pathlib
import sys
import math

sys.path.append(str(pathlib.Path(__file__).parent.parent.absolute()))

from acbmc.blender_operations.blender_scene_manipulator import BlenderSceneManipulator
from acbmc.blender_operations.model_build.max_builtin_blend_fbx_exp_comp_anim_char_const import \
 MaxBuiltinBlenderFbxExportComplianceAnimatedCharacterConstructor
from acbmc.model.animated_character.constructing.animated_character_description_loader \
    import AnimatedCharacterDescriptionLoader, AnimatedCharacterDescriptionLoaderForTesting
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription
from acbmc.model.animated_character.model.math.quaternion import Quaternion

from acbmc.model.animated_character.model.math.vector3d import Vector3d


class QuaternionRotationFactory:
    @classmethod
    def get_quaternion_rotate_angle_axis(cls, angle_radians: float, rotation_axis_arg: Vector3d) -> Quaternion:
        rotation_axis = rotation_axis_arg.normalized()

        qx = rotation_axis.x * math.sin(angle_radians / 2.0)
        qy = rotation_axis.y * math.sin(angle_radians / 2.0)
        qz = rotation_axis.z * math.sin(angle_radians / 2.0)
        qw = math.cos(angle_radians / 2.0)
        return Quaternion(w=qw, x=qx, y=qy, z=qz).normalized()


class SpaceTransformations:
    @staticmethod
    def position3d_transformation(vector3d: Vector3d):
        pass
        altered_vector3d = Vector3d(-vector3d.x, -vector3d.z, vector3d.y)
        vector3d.x = altered_vector3d.x
        vector3d.y = altered_vector3d.y
        vector3d.z = altered_vector3d.z

        # vector3d.y, vector3d.z = vector3d.z, vector3d.y

    @staticmethod
    def rotation_transformation(quaternion: Quaternion):
        pass

        # quaternion = Quaternion(1.0, 0.0, 0.0, 0.0)

        # quaternion.w = 1.0
        #quaternion.x = 0.0
        #quaternion.y = 0.0
        #quaternion.z = 0.0
        altered_quaternion = Quaternion(-quaternion.w, -quaternion.x, -quaternion.z, quaternion.y)
        #rotation_axis = Vector3d(x=0.0, y=0.0, z=-1.0).normalized()
        #rotation_angle = -(math.pi / 2)

        #altered_quaternion = \
        #(quaternion 
        #*   QuaternionRotationFactory.get_quaternion_rotate_angle_axis(
        #        angle_radians=rotation_angle,
        #        rotation_axis_arg=rotation_axis
        #    )
        #*   QuaternionRotationFactory.get_quaternion_rotate_angle_axis(
        #    angle_radians=rotation_angle,
        #    rotation_axis_arg=Vector3d(x=1.0, y=0.0, z=0.0).normalized()
        #    )
        #).normalized()

        quaternion.w = altered_quaternion.w
        quaternion.x = altered_quaternion.x
        quaternion.y = altered_quaternion.y
        quaternion.z = altered_quaternion.z
        
        # quaternion.y, quaternion.z = quaternion.z, quaternion.y


class ImportAnimatedCharacterLogic:
    def execute(self, filepath_to_import: str):
        animated_character_description = AnimatedCharacterDescriptionLoaderForTesting().load(filepath_to_import)  # type: AnimatedCharacterDescription
        BlenderSceneManipulator().clear_scene()
        animated_character_description.reform_space_model(
            position3d_transformation=SpaceTransformations.position3d_transformation,
            rotation_transformation=SpaceTransformations.rotation_transformation
        )
        animated_character_constructor = MaxBuiltinBlenderFbxExportComplianceAnimatedCharacterConstructor()
        animated_character_constructor.construct_animated_character(animated_character_description)


if __name__ == '__main__':
    ImportAnimatedCharacterLogic().execute()
