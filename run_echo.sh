#!/bin/bash
./buildtools/gn/linux64/gn gen out/Debug
ninja -C out/Debug echo
./mojo/public/tools/download_shell_binary.py
./mojo/public/tools/prebuilt/mojo_shell --origin=file://`pwd`/out/Debug "mojo://echo_client"
