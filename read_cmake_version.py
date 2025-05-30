import sys
import re

cmake_filename = sys.argv[1]        # e.g. CMake/vtkVersion.cmake
version_major_var = sys.argv[2]     # e.g. VTK_MAJOR_VERSION
version_minor_var = sys.argv[3]     # e.g. VTK_MINOR_VERSION
if len(sys.argv) > 4:
    version_patch_var = sys.argv[4]     # e.g. VTK_BUILD_VERSION

cmake_vars_regex = r'(set|SET\s*\()([^\s]+)[\s"]*([^)^"]+)'

with open(cmake_filename, 'r') as cmake_file:
    vars = dict(list(map(lambda varline: (re.search(cmake_vars_regex, varline).group(2), re.search(cmake_vars_regex, varline).group(3)), filter(lambda line: line.lower().startswith('set') and re.search(cmake_vars_regex, line) is not None, cmake_file.read().split('\n')))))

    major_version = vars[version_major_var]
    minor_version = vars[version_minor_var]
    if len(sys.argv) == 4:
        print(f'{major_version}.{minor_version}')

    if len(sys.argv) > 4:
        build_version = vars[version_patch_var]
        print(f'{major_version}.{minor_version}.{build_version}')