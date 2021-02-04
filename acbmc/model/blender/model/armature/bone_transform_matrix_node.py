from acbmc.util.model.matrix4x4 import Matrix4x4


class BoneTransformMatrixNode:
    def __init__(self):
        self.bone_name = None  # type: str
        self.bone_matrix = Matrix4x4.identity_matrix()  # type: Matrix4x4
        self.is_keyframe = False

    @staticmethod
    def from_matrix4x4(bone_name: str, matrix: Matrix4x4, is_keyframe: bool) -> 'BoneTransformMatrixNode':
        result = BoneTransformMatrixNode()
        result.bone_name = bone_name
        result.bone_matrix = matrix.copy()
        result.is_keyframe = is_keyframe
        return result
