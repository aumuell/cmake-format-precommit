"""A stand-in for the re.Scanner class.

cmakelang 0.6.13 builds its lexer with re.Scanner, whose use of capturing
groups is rejected by Python 3.15. This module installs a drop-in
replacement on the re module so that cmakelang can be imported and run
unchanged.

The semantics mirror re.Scanner.scan: patterns are tried in order at the
current position, a callable action receives (scanner, full_match), and a
zero-length match stops the scan, with the unscanned remainder returned.
"""

import re

PATCHED = False


class Scanner:
  def __init__(self, iters, flags=0):
    self.scanner = []
    for pattern, action in iters:
      if not isinstance(pattern, re.Pattern):
        pattern = re.compile(pattern, flags)
      self.scanner.append((pattern, action))
    self.match = None

  def scan(self, string):
    result = []
    pos = 0
    while True:
      advanced = False
      for pattern, action in self.scanner:
        m = pattern.search(string, pos)
        if m is None or m.start() != pos:
          continue
        self.match = m
        if callable(action):
          action = action(self, m.group())
        if action is not None:
          result.append(action)
        if m.end() == pos:
          return result, string[pos:]
        pos = m.end()
        advanced = True
        break
      if not advanced:
        return result, string[pos:]


def install():
  """Replace re.Scanner with this module's Scanner. Idempotent."""
  global PATCHED
  if not PATCHED:
    re.Scanner = Scanner
    PATCHED = True
