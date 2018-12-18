#!/bin/bash

# Clear old pkg content
rm -rf deb/

# Create pkg
mkdir -p deb/DEBIAN/
mkdir -p deb/usr/share/rime-data/
cp ./control deb/DEBIAN/
cp ./taigi.schema.yaml ./taigi.dict.yaml deb/usr/share/rime-data/

# Build pkg
dpkg -b deb/ rime-itaigi.deb
