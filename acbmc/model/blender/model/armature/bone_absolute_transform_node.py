from acbmc.util.model.transform_node import TransformNode


class BoneAbsoluteTransformNode:
    def __init__(self):
        self.bone_name = None  # type: str
        self.bone_transform = TransformNode()
