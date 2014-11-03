#!/bin/bash
./buildtools/gn gen out/Debug
./buildtools/ninja -C out/Debug echo
./mojo/public/tools/download_shell_binary.py
./mojo/public/tools/prebuilt/mojo_shell --origin=file://`pwd`/out/Debug "mojo://echo_client"
