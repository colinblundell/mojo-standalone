#!/bin/bash
example_name=$1
if [[ $example_name == "echo" ]]
then
  target_name="echo"
  library_name="echo_client"
elif [[ $example_name == "apptest" ]]
then
  target_name="apptest"
  library_name="example_apptests"
else
  echo "Unknown example: $example_name"
  exit 1
fi

./buildtools/gn gen out/Debug
./buildtools/ninja -C out/Debug $target_name
./buildtools/mojo_shell --origin=file://`pwd`/out/Debug "mojo://$library_name"
