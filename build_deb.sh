#!/bin/bash

# Clear old pkg content
rm -rf deb/

# Create pkg
mkdir -p deb/DEBIAN/
mkdir -p deb/usr/share/rime-data/
# deb package related file
cp ./control ./postinst ./postrm deb/DEBIAN/
# taigi
cp ./taigi.schema.yaml ./taigi.dict.yaml deb/usr/share/rime-data/
# copyright
cp ./LICENSE deb/DEBIAN/copyright

# Build pkg
rm -rf build/
mkdir build/
dpkg -b deb/ build/rime-taigi.deb

