from typing import Iterator, List, Optional, Tuple
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.tree_iteration_helper import TreeIterationHelper
from acbmc.util.model.transform_node import TransformNode
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.blender.model.armature.bone_absolute_transform_node import BoneAbsoluteTransformNode


class ArmatureBindPoseConsolidationHelper:
    @classmethod
    def iterate_non_present_tree_nodes_prepared_for_bind_pose_model_building(
        cls,
        armature_tree_hierarchy_to_consolidate_with: TreeHierarchy,
        result_armature_bind_pose_model: TreeHierarchy
    ) -> Iterator[Tuple[str, BoneAbsoluteTransformNode]]:
        non_present_nodes_names_set = \
            set(x.key for x in armature_tree_hierarchy_to_consolidate_with.iterate_nodes()) \
            .difference(
                set(x.key for x in result_armature_bind_pose_model.iterate_nodes())
            )

        parent_node_keys_node_tuples = []
        for node_key in non_present_nodes_names_set:
            node_info = armature_tree_hierarchy_to_consolidate_with.get_node(key=node_key)
            parent_node_keys_node_tuples.append((node_info.parent_key, node_key, node_info.node))

        result = []  # type: List[Tuple[Optional[str], str, BoneAbsoluteTransformNode]]
        for node_data in parent_node_keys_node_tuples:
            bone_name = node_data[1]  # type: str
            parent_bone_name = node_data[0] # type: Optional[str]
            node = node_data[2]  # type: BoneAbsoluteTransformNode
            if UnifiedArmatureWithDeformSetsBonesNamingHelper.is_channel_bone_name(bone_name):
                # center all channel bones in zero position, they only will be positioned and assigned properly in hierarchy
                # in particular animation clips later dynamically since that indeed may change
                result.append((parent_bone_name, bone_name, BoneAbsoluteTransformNode.get_zero_transform_with_bone_name(bone_name)))
            elif UnifiedArmatureWithDeformSetsBonesNamingHelper.is_deform_set_bone(bone_name):
                # for the sake of convenient artist work with our 3D model we can position subobjects in positions
                # as they were seen in first animation clip they actually first appeared, for each separate subobject respectively
                # deform set bones which govern subobjects skinning are governed by their parent channels, so in this case
                # we apply 'frozen' transform of parent channel bone to proper deform set bones, that should do the trick

                # important! we need to remember that such positioned bones can be in arbitrary transform really,
                # so that mesh itself will be messed up if we forget about it at this stage
                # because canonical 'home transform' for each subobject with its respective deform set bones
                # lies indeed in the origin of the space axes - we need somehow to overcome that!

                # screw that, we can make nice rest pose later down the line
                # simply position each subobject using its respective first-occurence animation clip
                # then apply armature modifier to all subobjects
                # and after that on Armature itself - apply pose as Rest Pose, and voila

                # on this stage position all channel bones in zero position in space
                # and each deform set bone of each subobject position using proper HOME transform, not deformed!
                # that is important! Then in next stage of constructing character model you will position meshes
                # that will fit such positioned deform set bones now that are in their bind poses respectively, and it all will click

                # yet another way:
                # on this stage simply consolidate all armature tree hierarchies as it was in the original idea
                # yet when we come to appending meshes later down the line
                # we will perform some tricks and tweaks with armature posing to adjust it eventually 
                # to that consolidated bind pose armature pose that we derive here, yet without inproper deformations
                # on subobjects' meshes - we will simply initially transform deform set bones to their actual bindposes
                # then skin meshes with them - that will give us correct initial deformations
                # then we will somehow deform armature after that to reflect this bind pose's armature tree hierarchy
                # and then:
                # 1. Apply armature modifier to all subobjects meshes
                # 2. Apply pose as Rest pose on the armature
                # that should work

                # if we won't do that, effect will be such that all channel bones will be at zero position
                # and all subobjects will be positioned in the beginning of the space axes as well
                # - ergo not very convenient for artist to work with in my opinion
                # - they need nice rest pose in the first place to work with

                # screw all the 'model after animations modifying stuff' - this won't work already with builtin Blender fbx export
                # here anyway - we will use Autodesk FBX SDK to implement dedicated FBX export for Blender

                if parent_bone_name is not None:
                    deform_set_bone_parent_channel_bone_transform = \
                        armature_tree_hierarchy_to_consolidate_with.get_node(key=parent_bone_name) \
                        .node.bone_transform.copy() # type: TransformNode
                    result.append((parent_bone_name, bone_name,
                        BoneAbsoluteTransformNode.from_transform_node(
                            bone_name, deform_set_bone_parent_channel_bone_transform)))
                else:
                    raise ValueError(
                        "Malformed armature hierarchy? Deform set bone seems to have" + \
                        " no parent channel bone associated in this particular hierarchy")
                    # result.append((parent_bone_name, bone_name, node.copy_as_bone_absolute_transform_node()))
            else:
                raise ValueError("Unrecognized bone name {} to associate armature node kind with it!".format(bone_name))

        result = list(TreeIterationHelper \
            .iterate_sequence_in_order_of_tree_building(
                collection=result,
                parent_key_getter=lambda element: element[0],
                node_key_getter=lambda element: element[1]))

        yield from [(x[1], x[2]) for x in result]
        
class UnifiedArtistConvenientDeformSetsArmatureBindPoseBuilder:
    def __init__(self):
        self._result = TreeHierarchy()

    def consider_armature_hierarchy_with_deform_sets(
        self, armature_tree_hierarchy: TreeHierarchy) -> 'UnifiedArtistConvenientDeformSetsArmatureBindPoseBuilder':

        for new_prepared_armature_tree_node in ArmatureBindPoseConsolidationHelper \
            .iterate_non_present_tree_nodes_prepared_for_bind_pose_model_building(
                armature_tree_hierarchy, self._result
            ):
            self._result.add_node(
                parent_key=None, node_key=new_prepared_armature_tree_node[0],
                node=new_prepared_armature_tree_node[1])

        return self

    def build(self) -> TreeHierarchy:
        return self._result
