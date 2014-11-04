#!/usr/bin/env python
# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys
from utils import commit
from utils import mojo_root_dir
from utils import system

dirs_to_clone = [
  "mojo/public",
]

def rev(source_dir, target_dir):
  os.chdir(source_dir)
  src_commit = system(["git", "show-ref", "HEAD", "-s"]).strip()

  for d in dirs_to_clone:
    print "removing directory %s" % d
    os.chdir(target_dir)
    system(["git", "rm", "-r", d])
    print "cloning directory %s" % d
    os.chdir(source_dir)
    files = system(["git", "ls-files", d])
    for f in files.splitlines():
      dest_path = os.path.join(target_dir, f)
      system(["mkdir", "-p", os.path.dirname(dest_path)])
      system(["cp", os.path.join(source_dir, f), dest_path])
    os.chdir(target_dir)
    system(["git", "add", d])

  os.chdir(target_dir)
  with open("MOJO_SDK_VERSION", "w") as version_file:
    version_file.write(src_commit)
  system(["git", "add", "MOJO_SDK_VERSION"])
  commit("Update mojo sdk to rev " + src_commit)

if len(sys.argv) != 1:
  print "usage: rev_sdk.py <mojo source dir>"
  sys.exit(1)

rev(sys.argv[1], root_dir)
