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
# Copy markdown and PDF files (exclude templates and base.md)
for file in course_wide/*.md; do
    basename=$(basename "$file")
    if [[ "$basename" != *"_template.md" && "$basename" != "base.md" ]]; then
        cp "$file" mooc/course_wide/
    fi
done 2>/dev/null || true
cp course_wide/*.pdf mooc/course_wide/ 2>/dev/null || true
