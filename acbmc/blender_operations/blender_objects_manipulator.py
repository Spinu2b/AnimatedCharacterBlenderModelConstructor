import bpy
from bpy.types import ID, Object

class BlenderObjectsManipulator:
    def create_new_object_with_linked_datablock(
        self, object_name: str, data_block: ID) -> Object:
        return bpy.data.objects.new(name=object_name, object_data=data_block)

    def link_object_to_the_scene(self, object: Object):
        bpy.context.collection.objects.link(object=object)

    def deselect_all_objects(self):
        bpy.ops.object.select_all(action='DESELECT')

    def deselect_all_pose_objects(self):
        bpy.ops.pose.select_all(action='DESELECT')

    def select_all_pose_objects(self):
        bpy.ops.pose.select_all(action='SELECT')

    def set_active_object_to(self, object: Object):
        bpy.context.view_layer.objects.active = object

    def select_active_object(self, object: Object):
        bpy.context.active_object.select_set(state=True)

    def parent_object_to(self, child: Object, parent: Object):
        child.parent = parent
