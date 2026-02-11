#!/bin/bash
set -e

mkdir mooc
cd lecture
bash render.sh
cd ..
cd labs
bash render.sh
cd ..
mkdir -p mooc/support
cp -r lecture/support/web mooc/support/web
cp -r lecture/support/misc mooc/support/misc
cp -r lecture/support/pdf mooc/pdf
cp -r lecture/support/pptx mooc/pptx
cp -r lecture/support/md mooc/md
cp -r labs mooc/labs
cp -r course_wide mooc/course_wide
