#!/bin/bash

function install_build_dep {
  SRC_URL=$1
  PACKAGE_DIR=$2
  ROOT_DIR="$(dirname $(realpath $(dirname "${BASH_SOURCE[0]}")))"
  FILENAME="$(basename $SRC_URL)"

  BUILD_DIR="$(basename $FILENAME .tar.gz)"
  THIRD_PARTY="$ROOT_DIR/third_party/"
  INSTALL_DIR="$THIRD_PARTY/$PACKAGE_DIR"
  OUT_DIR="$INSTALL_DIR/$BUILD_DIR/$PACKAGE_DIR"
  OLD_DIR="$THIRD_PARTY/$PACKAGE_DIR.old"

  mkdir -p "$INSTALL_DIR"
  cd "$INSTALL_DIR"
  echo "Downloading $SRC_URL"
  curl --remote-name "$SRC_URL"
  tar xvzf "$FILENAME"

  cd "$BUILD_DIR/$PACKAGE_DIR"

  # Replace with new directory
  cd "$ROOT_DIR"
  mv "$INSTALL_DIR" "$OLD_DIR"
  mv "$OLD_DIR/$BUILD_DIR/$PACKAGE_DIR" "$INSTALL_DIR"
  rm -fr "$OLD_DIR"

}

# Download and extract PLY
# Homepage:
# http://dabeaz.com/ply
install_build_dep "http://dabeaz.com/ply/ply-3.4.tar.gz" "ply"

# Download and extract Jinja2
# Homepage:
# http://jinja.pocoo.org/
# Installation instructions:
# http://jinja.pocoo.org/docs/intro/#from-the-tarball-release
# Download page:
# https://pypi.python.org/pypi/Jinja2
JINJA2_SRC_URL="https://pypi.python.org/packages/source/"
JINJA2_SRC_URL+="J/Jinja2/Jinja2-2.7.1.tar.gz"
install_build_dep $JINJA2_SRC_URL 'jinja2'
