#!/bin/bash

# Clear old pkg content
rm -rf deb/

# Create pkg
mkdir -p deb/DEBIAN/
mkdir -p deb/usr/share/rime-data/
cp ./control deb/DEBIAN/
cp ./taigi.schema.yaml ./taigi.dict.yaml deb/usr/share/rime-data/
cp ./LICENSE deb/DEBIAN/copyright

# Build pkg
rm -rf build/
mkdir build/
dpkg -b deb/ build/rime-itaigi.deb

