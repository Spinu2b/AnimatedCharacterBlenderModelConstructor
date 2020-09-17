from acbmc.entrypoint import ImportAnimatedCharacterLogic


class BlenderAddonLogicRunner:
    def execute(self):
        filepath = "D:\\RaymapExports\\[rayman] YLT_RaymanModel _ Rayman.animperso"
        ImportAnimatedCharacterLogic().execute(filepath_to_import=filepath)
