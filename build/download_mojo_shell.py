#!/usr/bin/env python
# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess
import sys
import tempfile
import zipfile

current_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.join(current_path, "..")

if not sys.platform.startswith("linux"):
  print "Not supported for your platform"
  sys.exit(0)

# TODO(blundell): Re-enable this logic once VERSION is restored in the Mojo 
# repo. For now, hardcode to the last known Mojo shell version.
#version_path = os.path.join(root_path, "mojo/public/VERSION")
#with open(version_path) as version_file:
#  version = version_file.read().strip()
version = "e6ea280f719b61120da513e3ce0371b911f85f11"

mojo_shell_path = os.path.join(root_path, "buildtools")
stamp_path = os.path.join(mojo_shell_path, "MOJO_SHELL_VERSION")

try:
  with open(stamp_path) as stamp_file:
    current_version = stamp_file.read().strip()
    if current_version == version:
      sys.exit(0)
except IOError:
  pass

platform = "linux-x64" # TODO: configurate
basename = platform + ".zip"

gs_path = "gs://mojo/shell/" + version + "/" + basename

gsutil_exe = os.path.join(root_path, "third_party", "gsutil", "gsutil")

with tempfile.NamedTemporaryFile() as temp_zip_file:
  subprocess.check_call([gsutil_exe, "cp", gs_path, temp_zip_file.name])
  with zipfile.ZipFile(temp_zip_file.name) as z:
    zi = z.getinfo("mojo_shell")
    mode = zi.external_attr >> 16L
    z.extract(zi, mojo_shell_path)
    os.chmod(os.path.join(mojo_shell_path, "mojo_shell"), mode)

with open(stamp_path, 'w') as stamp_file:
  stamp_file.write(version + "\n")
