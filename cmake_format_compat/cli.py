"""Entry points that install the re.Scanner shim before running cmakelang.

They override the console scripts shipped by cmakelang so that the
formatter and linter work on Python versions where re.Scanner no longer
accepts the patterns cmakelang uses.
"""

import cmake_format_compat  # noqa: F401  (installs the shim)

from cmakelang.format.__main__ import main as format_main
from cmakelang.lint.__main__ import main as lint_main


def cmake_format():
  raise SystemExit(format_main())


def cmake_lint():
  raise SystemExit(lint_main())
