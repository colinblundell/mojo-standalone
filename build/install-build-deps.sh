#!/bin/bash

ROOT_DIR="$(dirname $(realpath $(dirname "${BASH_SOURCE[0]}")))"

function install_dep_from_tarfile {
  SRC_URL=$1
  PACKAGE_DIR=$2
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

# BODY

# Install gn.
~/depot_tools/download_from_google_storage --bucket chromium-gn --output $ROOT_DIR/buildtools/gn/linux64/gn 56e78e1927e12e5c122631b7f5a46768e527f1d2

# Download and extract PLY
# Homepage:
# http://dabeaz.com/ply
install_dep_from_tarfile "http://dabeaz.com/ply/ply-3.4.tar.gz" "ply"

# Download and extract Jinja2
# Homepage:
# http://jinja.pocoo.org/
# Installation instructions:
# http://jinja.pocoo.org/docs/intro/#from-the-tarball-release
# Download page:
# https://pypi.python.org/pypi/Jinja2
JINJA2_SRC_URL="https://pypi.python.org/packages/source/"
JINJA2_SRC_URL+="J/Jinja2/Jinja2-2.7.1.tar.gz"
install_dep_from_tarfile $JINJA2_SRC_URL 'jinja2'
