from typing import Dict


class SubobjectUsedMorphAssociationInfo:
    def __init__(self):
        self.morph_subobject_start = -1  # type: int
        self.morph_subobject_end = -1  # type: int
        self.morph_progress_keyframes = dict()  # type: Dict[int, float]
