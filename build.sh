#!/bin/bash
set -e

mkdir mooc
cd mooc_src
bash render.sh
cd ..
cp -r mooc_src/support mooc/support
cp -r mooc_src/pdf mooc/pdf
cp -r mooc_src/pptx mooc/pptx
cp -r mooc_src/md mooc/md
cp -r labs mooc/labs
cp -r course_wide mooc/course_wide
