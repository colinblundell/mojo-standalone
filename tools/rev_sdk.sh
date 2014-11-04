#!/bin/bash
ROOT_DIR="$(dirname $(realpath $(dirname "${BASH_SOURCE[0]}")))"
CHROMIUM_SRC_DIR=$1
MOJO_SRC_DIR=$2

VERSION_FILE=$CHROMIUM_SRC_DIR/mojo/public/VERSION
VERSION=`cat $VERSION_FILE`

cd $MOJO_SRC_DIR
git checkout $VERSION

cd $ROOT_DIR
./tools/rev_sdk.py $MOJO_SRC_DIR
