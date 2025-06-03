# Usage:
#   read_cmake_version.py CMakeLists.txt STELLARIUM_MAJOR STELLARIUM_MINOR
#   read_cmake_version.py CMakeLists.txt project

import sys
import re
import os

cmake_vars_regex = r'([set|SET]\s*\()([^\s]+)[\s"]*([^)^"]+)'
cmake_project_definition_regex = r'(project\s*\()([^\s]+)\sVERSION\s+([^\s^)^"]+)'

if __name__ == '__main__':
    cmake_filename = sys.argv[1]

    def read_project_version():
        with open(cmake_filename, 'r') as cmake_file:
            project_def = list(filter(lambda line: line.lower().startswith('project') and re.search(cmake_project_definition_regex, line) is not None, cmake_file.read().split('\n')))[0]
            project_version = re.search(cmake_project_definition_regex, project_def).group(3)
            print(project_version)

    def read_from_cmake_variables():
        print(os.popen('ls').read())
        try:
            version_vars = []
            argindex = 2
            while argindex < len(sys.argv):
                version_vars.append(sys.argv[argindex])
                argindex += 1

            with open(cmake_filename, 'r') as cmake_file:
                vars = dict(list(map(lambda varline: (re.search(cmake_vars_regex, varline).group(2), re.search(cmake_vars_regex, varline).group(3)), filter(lambda line: line.lower().startswith('set') and re.search(cmake_vars_regex, line) is not None, cmake_file.read().split('\n')))))

                version = []
                for version_var in version_vars:
                    version.append(vars[version_var])

                print('.'.join(version))

        except Exception as e:
            print(f'Error trying to read version variables {version_vars} from cmake file {cmake_filename}:\n{e}.\nVariables found:')
            for var in vars.keys():
                value = vars[var]
                print(f'\t{var}={value}')

    if sys.argv[2] == 'project':
        read_project_version()
    else:
        read_from_cmake_variables()
