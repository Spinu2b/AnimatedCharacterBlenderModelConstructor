from acbmc.util.model.tree_hierarchy import TreeHierarchy


class UnifiedArmatureTreeHierarchyToOnlyDeformSetBonesFlattener:
    # https://blender.stackexchange.com/questions/44637/how-can-i-manually-calculate-bpy-types-posebone-matrix-using-blenders-python-ap
    """
    armature.data.bones["Bone"].matrix_local
    Is the bone's world un-posed matrix (the pose_bone.matrix in rest state).

    armature.pose.bones["Bone"].matrix_basis
    Is the bone's local pose matrix.

    From there we can calculate any bone's world matrix by recursively traversing it's parents. Note: This will not include any constraints or IK (but it will include drivers or actions):

    def matrix_world(armature_ob, bone_name):
        local = armature_ob.data.bones[bone_name].matrix_local
        basis = armature_ob.pose.bones[bone_name].matrix_basis

        parent = armature_ob.pose.bones[bone_name].parent
        if parent == None:
            return  local * basis
        else:
            parent_local = armature_ob.data.bones[parent.name].matrix_local
            return matrix_world(armature_ob, parent.name) * (parent_local.inverted() * local) 
    """

    # https://blenderartists.org/t/how-to-global-pose-transforms-to-hierarchial-armature/548022/5
    # https://veeenu.github.io/blog/implementing-skeletal-animation/
    
    """
        def position_bone_in_animation_frame(
            self,
            armature_obj: Object,
            animation_frame_armature_bone_model: 'BlenderPoseModeAnimationFrameModelNode'):
        pose = armature_obj.pose  # type: Pose
        complementary_pose_bone = pose.bones.get(animation_frame_armature_bone_model.bone_name)  # type: PoseBone
        complementary_pose_bone.rotation_mode = 'QUATERNION'

        if animation_frame_armature_bone_model.bone_name != "ROOT_CHANNEL":
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
            world_mat = loc @ rot @ scale
            complementary_pose_bone.matrix = armature_obj.convert_space(
                pose_bone=complementary_pose_bone,
                matrix=world_mat,
                from_space='WORLD',
                to_space='POSE')
    """

    # https://stackoverflow.com/questions/11920866/global-transform-to-local-transform

    """
    Just multiply the object's world transform matrix by the inverse of parent's world transform:

        M_loc = M_parent_inv * M

    So - initially calculate world matrix for each bone separately in the armature hierarchy - the solution is given a bit above
    Then, consequently traverse hierarchy from top to bottom calculating local matrices for each bone
    in the hierarchy - that will get the matrices that you will need to later assign to pose bones to their 'matrix' property
    like in listing above - in that situation above we used convert_space method from Blender API since we operated there
    on pose bones - in current case we need to do it mathematically since we operate on our own model here

    You can get local matrices by combining TransformNode's components (position, rotation, scale)
    In the current context at the moment of writing this comment (23-11-2020 23:20) the context of using those objects
    is that we use local transforms :P

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

    ------------------------------------------------------------------------------------------

    Once you have world matrices for deform set bones, calculate pose local matrices for them
    considering only two-noded parenting chain - global root bone for the armature and a appropriate deform set bone below it
    - without involvement of intermediate channel bones - simply without them, regardless whether it would be one-rooted or multi-rooted eventually
    """

    @classmethod
    def flatten_armature_to_using_only_deform_set_bones_using_channel_bones_transforms_parenting_chains(
        cls, armature_tree_hierarchy: TreeHierarchy
    ):
        raise NotImplementedError
