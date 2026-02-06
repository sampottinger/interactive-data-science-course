#!/bin/bash
set -e

mkdir mooc
cd mooc_src
bash render.sh
cd ..
mkdir -p mooc/support
cp -r mooc_src/support/web mooc/support/web
cp -r mooc_src/support/misc mooc/support/misc
cp -r mooc_src/support/pdf mooc/pdf
cp -r mooc_src/support/pptx mooc/pptx
cp -r mooc_src/support/md mooc/md
cp -r labs mooc/labs
cp -r course_wide mooc/course_wide
