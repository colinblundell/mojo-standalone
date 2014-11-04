#!/bin/bash
./buildtools/gn gen out/Debug
./buildtools/ninja -C out/Debug $1
./buildtools/mojo_shell --origin=file://`pwd`/out/Debug "mojo://$2"
