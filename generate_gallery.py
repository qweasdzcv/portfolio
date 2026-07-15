import os
from pathlib import Path

roots = {
    'book': Path('image/书籍设计'),
    'brand': Path('image/品牌设计'),
    'ip': Path('image/ip形象设计'),
    'illustration': Path('image/插画'),
}

order = ['book', 'brand', 'ip', 'illustration']
labels = {'book':'书籍设计','brand':'品牌设计','ip':'IP形象','illustration':'插画设计'}

for cat in order:
    root = roots[cat]
    print(f'// {labels[cat]}')
    for dirpath, _, filenames in os.walk(root):
        for f in sorted(filenames):
            if f.lower().endswith(('.jpg','.jpeg','.png','.gif','.webp','.bmp')):
                p = os.path.join(dirpath, f).replace('\\','/').replace('\\','/')
                print(p)
    print()
