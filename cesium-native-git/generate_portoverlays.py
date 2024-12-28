import json
import os
import sys

working_dir = sys.argv[1]
overlays_dir = f'{working_dir}/overlays'

def run(cmd):
    output = os.popen(cmd).read()
    return output

vcpkg_template = """
{
    "name": "%s",
    "version": "%s"
}
"""

dependencies = { 
    'abseil': '20240722.0',
    'draco': '1.5.6',
    'fmt': '11.0.2',
    'libwebp': '1.5.0',
    'meshoptimizer': '0.22',
    's2geometry': '0.11.1',
    'spdlog': '1.10.0',
    'tinyxml2': '2.6.2',
    'uriparser': '0.9.8'
}

run(f'mkdir -p {overlays_dir}')

for dependency in dependencies.keys():
    version = dependencies[dependency]
    run(f'mkdir -p {overlays_dir}/{dependency}')
    vcpkg = vcpkg_template % (dependency, version)    
    with open(f'{overlays_dir}/{dependency}/vcpkg.json', 'w+') as vcpkgfile:  
        vcpkgfile.write(vcpkg)
    print(f'Wrote {overlays_dir}/{dependency}/vcpkg.json with content: {vcpkg}')

    with open(f'{overlays_dir}/{dependency}/portfile.cmake', 'w+') as portfile:  
        portfile.write('set(VCPKG_POLICY_EMPTY_PACKAGE enabled)')
    print(f'Wrote {overlays_dir}/{dependency}/portfile.cmake.')
