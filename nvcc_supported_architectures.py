import os

architectures = list(map(lambda arch: arch.replace('compute_', ''), os.popen('nvcc --list-gpu-arch').read().strip().split('\n')))
print(';'.join(architectures))
