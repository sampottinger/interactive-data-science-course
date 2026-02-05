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
cd course_wide
bash render.sh
cd ..
mkdir -p mooc/course_wide
# Copy only rendered HTML files (exclude templates, base.html, render scripts)
for file in course_wide/*.html; do
    basename=$(basename "$file")
    if [[ "$basename" != *"_template.html" && "$basename" != "base.html" ]]; then
        cp "$file" mooc/course_wide/
    fi
done
# Copy markdown and PDF files if they exist
cp course_wide/*.md mooc/course_wide/ 2>/dev/null || true
cp course_wide/*.pdf mooc/course_wide/ 2>/dev/null || true
