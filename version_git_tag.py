import os
import sys


class Version:
    def __init__(self, verstr):
        if verstr.startswith('v'):
            verstr = verstr[1:]
        self.majorver = int(verstr.split('.')[0])
        self.minorver = int(verstr.split('.')[1])
        self.patchver = int(verstr.split('.')[2])

    def __comp__ (self, other):
        if self.majorver != other.majorver:
            return self.majorver - other.majorver
        elif self.minorver != other.minorver:
            return self.minorver - other.minorver
        else:
            return self.patchver - other.patchver

    def __gt__(self, other):
        return self.__comp__(other) > 0

    def __repr__(self):
        return f'{str(self.majorver)}.{str(self.minorver)}.{str(self.patchver)}'

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    gitrepodir = sys.argv[1]
    print(f'Looking for version defined in Git repo at {gitrepodir}.')
    verstrs = os.popen(f'cd {gitrepodir} && git tag').read().strip().split('\n')
    versions = list(map(lambda verstr: Version(verstr), filter(lambda verstr: len(verstr) > 0, verstrs)))
    versions.sort()
    #print('Found versions: ' + ','.join(map(lambda version: f'{version}', versions)))
    version = versions[-1]
    version.patchver += 1
    print(version)