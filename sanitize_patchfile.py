import sys
import os
EXCLUDE_LINE_PREFIXES = ['IDEA additional info:', 'Subsystem:', 'Subject:', 'diff --git']

patchfilename = sys.argv[1]
patchfilename_orig = patchfilename.replace('.patch', '.patch.orig')
os.popen(f'cp {patchfilename} {patchfilename_orig}').read()

def exclude_line(line):
    for prefix in EXCLUDE_LINE_PREFIXES:
        if line.startswith(prefix):
            return True

    return False

def map_line(line):
    if line.startswith('--- a/'):
        line = line.replace('--- a/', '--- ')
    elif line.startswith('+++ b/'):
        line = line.replace('+++ b/', '+++ ')
    return line

with open(patchfilename, 'r') as patchfile:
    lines = patchfile.read().split('\n')
    filtered = list(map(lambda line: map_line(line), filter(lambda line: not exclude_line(line), lines)))

with open(patchfilename, 'w') as patchfile:
    patchfile.write('\n'.join(filtered))