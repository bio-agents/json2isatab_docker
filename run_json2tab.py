import sys
import os
src_json = sys.argv[1]
target_dir = sys.argv[2]
try:
    from isaagents.convert import json2isatab
except ImportError as e:
    raise RuntimeError("Could not import isaagents package")
json2isatab.convert(open(src_json), target_dir)
