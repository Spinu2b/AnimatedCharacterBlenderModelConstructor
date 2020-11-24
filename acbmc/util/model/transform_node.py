import mathutils
from acbmc.util.model.matrix4x4 import Matrix4x4
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d


class TransformNode:
    def __init__(self):
        self.position = Vector3d()
        self.rotation = Quaternion()
        self.scale = Vector3d(1.0, 1.0, 1.0)

    """
    loc = Matrix.Translation(Vector((
                animation_frame_armature_bone_model.position.x,
                animation_frame_armature_bone_model.position.y,
                animation_frame_armature_bone_model.position.z)))
            rot = Quaternion(Vector((
                animation_frame_armature_bone_model.rotation.w,
                animation_frame_armature_bone_model.rotation.x,
                animation_frame_armature_bone_model.rotation.y,
                animation_frame_armature_bone_model.rotation.z)),
                ).to_matrix().to_4x4()
            scale = Matrix()
            scale[0][0] = animation_frame_armature_bone_model.scale.x
            scale[1][1] = animation_frame_armature_bone_model.scale.y
            scale[2][2] = animation_frame_armature_bone_model.scale.z
            local_transformation_matrix = loc @ rot @ scale
    """
    def get_matrix(self) -> Matrix4x4:
        location = mathutils.Matrix.Translation(mathutils.Vector((self.position.x, self.position.y, self.position.z)))
        rotation = mathutils.Quaternion(
            mathutils.Vector((self.rotation.w, self.rotation.x, self.rotation.y, self.rotation.z))).to_matrix().to_4x4()
        scale = mathutils.Matrix()
        scale[0][0] = self.scale.x
        scale[1][1] = self.scale.y
        scale[2][2] = self.scale.z
        result = location @ rotation @ scale
        return Matrix4x4.from_blender_matrix(result)

    @staticmethod
    def lerp(transform_a: 'TransformNode', transform_b: 'TransformNode', interpolation: float) -> 'TransformNode':
        result = TransformNode()
        result.position = Vector3d.lerp(transform_a.position, transform_b.position, interpolation)
        result.rotation = Quaternion.lerp(transform_a.rotation, transform_b.rotation, interpolation)
        result.scale = Vector3d.lerp(transform_a.scale, transform_b.scale, interpolation)
        return result

    def copy(self) -> 'TransformNode':
        result = TransformNode()
        result.position = self.position.copy()
        result.rotation = self.rotation.copy()
        result.scale = self.scale.copy()
        return result
