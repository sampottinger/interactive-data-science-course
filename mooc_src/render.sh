python3 ./render.py index ./index.html ./course.yml ../mooc/index.html

for i in {1..25}; do
    python3 ./render.py lesson ./lesson.html ./course.yml $i ../mooc/lesson$i.html
 done