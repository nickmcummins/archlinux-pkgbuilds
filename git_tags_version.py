import os
import sys

dir = sys.argv[1]

git_tag = os.popen(f'cd {dir} && git describe --long --tags').read().strip()
git_tag = git_tag[0:git_tag.index('-')]
git_tag = git_tag.replace('v', '')
print(git_tag)

