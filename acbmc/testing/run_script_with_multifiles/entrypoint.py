# This works!

import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.parent.absolute()))

from acbmc.testing.run_script_with_multifiles.testmodule import another_module_test_function

another_module_test_function()
