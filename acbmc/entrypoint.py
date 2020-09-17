import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.absolute()))

class ImportAnimPersoLogic:
    def execute(self, filepath_to_import: str):
        print("Hello world!")


if __name__ == '__main__':
    ImportAnimPersoLogic().execute()
