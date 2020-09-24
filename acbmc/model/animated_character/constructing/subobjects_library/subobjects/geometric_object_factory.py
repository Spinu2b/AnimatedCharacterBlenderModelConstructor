from typing import Dict, List
from acbmc.model.animated_character.constructing.subobjects_library.subobjects.geometric_object.bone_bind_pose_factory import BoneBindPoseFactory
from acbmc.model.animated_character.constructing.math.vector2d_factory import Vector2DFactory
from acbmc.model.animated_character.constructing.math.vector3d_factory import Vector3dFactory
from acbmc.model.animated_character.model.subobjects_library_desc.subobject_desc.geo_obj_desc.bone_bind_pose import BoneBindPose
from acbmc.model.animated_character.model.math.vector2d import Vector2d
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.model.animated_character.model.subobjects_library_desc.subobject_desc.geometric_object import GeometricObject


class GeometricObjectFactory:
    def construct_from_json_dict(self, geometric_object_json_dict) -> GeometricObject:
        result = GeometricObject()
        result.vertices = self._get_vertices(geometric_object_json_dict["vertices"])
        result.normals = self._get_normals(geometric_object_json_dict["normals"])
        result.triangles = self._get_triangles(geometric_object_json_dict["triangles"])
        result.uv_maps = self._get_uv_maps(geometric_object_json_dict["uvMaps"])
        result.material = geometric_object_json_dict["material"]

        result.bind_bone_poses = self._get_bind_bone_poses(geometric_object_json_dict["bindBonePoses"])
        result.bone_weights = self._get_bone_weights(geometric_object_json_dict["boneWeights"])
        return result

    def _get_vertices(self, vertices_json_dict) -> List[Vector3d]:
        vector3d_factory = Vector3dFactory()
        return [vector3d_factory.construct_from_json_dict(x) for x in vertices_json_dict]

    def _get_normals(self, normals_json_dict) -> List[Vector3d]:
        vector3d_factory = Vector3dFactory()
        return [vector3d_factory.construct_from_json_dict(x) for x in normals_json_dict]

    def _get_triangles(self, triangles_json_dict) -> List[int]:
        return [x for x in triangles_json_dict]

    def _get_uv_maps(self, uv_maps_json_dict) -> List[List[Vector2d]]:
        vector2d_factory = Vector2DFactory()
        return [[vector2d_factory.construct_from_json_dict(y) for y in x] for x in uv_maps_json_dict]

    def _get_bind_bone_poses(self, bind_bone_poses_json_dict) -> Dict[int, BoneBindPose]:
        bone_bind_pose_factory = BoneBindPoseFactory()
        return {k:bone_bind_pose_factory.construct_from_json_dict(v) for (k,v) in bind_bone_poses_json_dict.items()}

    def _get_bone_weights(self, bone_weights_json_dict) -> Dict[int, Dict[int, float]]:
        return {outer_key:{inner_key:inner_value for (inner_key,inner_value) in outer_value.items()} for (outer_key,outer_value)
         in bone_weights_json_dict.items()}
