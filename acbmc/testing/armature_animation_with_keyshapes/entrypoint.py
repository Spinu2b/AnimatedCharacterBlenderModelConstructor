import pathlib
import sys
from typing import List
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.parent.absolute()))

from acbmc.blender_operations.blender_fbx_export import BlenderFbxExport
from acbmc.blender_operations.blender_file_manipulator import BlenderFileManipulator
from acbmc.utils.space.space_models import SpaceModels, SpaceModel
from acbmc.utils.testing_utils.cube_geometry_factory import CubeGeometryFactory
from acbmc.utils.testing_utils.armature_key_shapes_animated_test_cube_builder import\
    ArmatureKeyShapesAnimatedTestCubeBuilder
from acbmc.blender_operations.blender_scene_manipulator import BlenderSceneManipulator
from acbmc.utils.geometry.geometry_description_manipulator import GeometryDescriptionManipulator
from acbmc.utils.math.quaternion import Quaternion
from acbmc.utils.math.transform import Transform, TransformBuilder
from acbmc.utils.math.vector3d import Vector3d


class ArmatureAnimationWithKeyshapesTestCase:
    def __init__(self):
        self.initial_bone_transform = TransformBuilder()\
            .set_position(Vector3d(0.0, 0.0, 0.0)) \
            .set_rotation(Quaternion(1.0, 0.0, 0.0, 0.0)) \
            .set_scale(Vector3d(0.0, 0.0, 0.0)) \
            .build()  # type: Transform
        self.initial_cube_vertices = CubeGeometryFactory().get_cube_default_vertices()  # type: List[Vector3d]
        self.space_model = SpaceModels.get_blender_space_model()  # type: SpaceModel

        raise NotImplementedError

    def run_test_case(self):
        BlenderSceneManipulator().clear_scene()
        ArmatureKeyShapesAnimatedTestCubeBuilder() \
            .set_bone_keyframe(
                frame=0,
                absolute_transform=self.initial_bone_transform) \
            .set_bone_keyframe(
                frame=10,
                absolute_transform=Transform.translate_by(
                    transform=self.initial_bone_transform,
                    offset=self.space_model.get_forward_vector() * 5)) \
            .set_keyshape(
                frame=0,
                vertices=self.initial_cube_vertices) \
            .set_keyshape(
                frame=10,
                vertices=GeometryDescriptionManipulator.scale(
                    scale_factor=2.0,
                    vertices=self.initial_cube_vertices)
            ).instantiate()
        BlenderFileManipulator().save_blend_file(filepath=self.blend_output_file_path)
        BlenderFbxExport().export_to_fbx_file(filepath=self.fbx_output_file_path)


if __name__ == '__main__':
    ArmatureAnimationWithKeyshapesTestCase().run_test_case()
