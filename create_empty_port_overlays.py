import os
import sys
import json

if __name__ == '__main__':
    vcpkg_json = sys.argv[1]
    vcpkg_deps = sys.argv[2].split(',') if len(sys.argv) > 2 else []
    srcdir = os.getcwd()

    with open(vcpkg_json, 'r', encoding='utf-8-sig') as vcpkgdef:
        dependencies = list(filter(lambda dep: not dep in vcpkg_deps, json.loads(vcpkgdef.read())['dependencies']))

    for pkg in dependencies:
        pkgname = pkg if pkg.__class__ == str else pkg['name']
        print(pkgname)

        pkg_portoverlay = f'{srcdir}/extern/vcpkg/ports/{pkgname}'

        if not os.path.exists(pkg_portoverlay):
            os.popen(f'mkdir -p {pkg_portoverlay}').read()

        if not os.path.exists(f'{pkg_portoverlay}/vcpkg.json'):
            with open(f'{pkg_portoverlay}/vcpkg.json', 'w') as vcpkg:
                if pkg.__class__ == str:
                    vcpkg.write("""
            {
                "name": "%s",
                "version": "1.0.0"
            }""" % (pkgname))
                else:
                    print(pkg)
                    print(len(pkg))
                    print(str(pkg))
                    if 'version' not in pkg.keys():
                        pkg['version'] = '1.0.0'
                    vcpkg.write(json.dumps(pkg))

        if not os.path.exists(f'{pkg_portoverlay}/portfile.cmake'):
            with open(f'{pkg_portoverlay}/portfile.cmake', 'w') as portfile:
                portfile.write('set(VCPKG_POLICY_EMPTY_PACKAGE enabled)')