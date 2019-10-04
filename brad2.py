import os
import json

toolchains = set([
"ninja-vs-15-2017-win64-cxx17",
"nmake-vs-15-2017-win64-cxx17",
"vs-15-2017-win64-cxx17",
"vs-14-2015-sdk-8-1",
"mingw-cxx17",
"msys-cxx17",
"clang-cxx17",
"gcc-7-cxx17",
"android-ndk-r17-api-24-arm64-v8a-clang-libcxx14",
"analyze-cxx17",
"sanitize-address-cxx17",
"sanitize-leak-cxx17",
"sanitize-thread-cxx17",
"osx-10-13-make-cxx14",
"osx-10-13-cxx14",
"ios-nocodesign-11-4-dep-9-3"
])

for example in os.listdir('examples'):
	print(example)

	if not os.path.exists('examples/{}/.travis.yml'.format(example)):
		print('Skipping')
		continue

	travis = open('examples/{}/.travis.yml'.format(example)).readlines()
	travis = [line.strip() for line in travis if not line.strip().startswith('#')]
	travis = set([line.split('TOOLCHAIN=')[1].split()[0] for line in travis if 'TOOLCHAIN=' in line])
	print(travis)

	appveyor = open('examples/{}/appveyor.yml'.format(example)).readlines()
	appveyor = [line.strip() for line in appveyor if not line.strip().startswith('#')]
	appveyor = set([line.split('TOOLCHAIN:')[1].strip().replace('"', '') for line in appveyor if 'TOOLCHAIN:' in line])
	print(appveyor)

	blacklist = sorted([toolchain for toolchain in toolchains if toolchain not in appveyor and toolchain not in travis])
	print(blacklist)

	with open('examples/{}/.ci'.format(example), 'w') as f:
		f.write(json.dumps({"blacklist": blacklist}, sort_keys=True, indent=4, separators=(',', ': ')))
