

from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.animated_character.model.animation_clips_desc.channel_transform import ChannelTransform
from acbmc.model.blender.model.armature.bone_absolute_transform_node import BoneAbsoluteTransformNode


class ArmatureTreeHierarchyNode(BoneAbsoluteTransformNode):
    def __init__(self):
        super().__init__()

    @staticmethod
    def from_channel_transform(bone_name: str, channel_transform: ChannelTransform) -> 'ArmatureTreeHierarchyNode':
        result = ArmatureTreeHierarchyNode()
        result.bone_name = bone_name
        result.bone_transform = channel_transform.copy_as_pure_transform_node()
        return result


class ArmatureTreeHierarchy(TreeHierarchy):
    pass
