#!/usr/bin/env python3
import subprocess

# git remote add ingenue https://github.com/ingenue/hunter.git
# git fetch ingenue
# git branch -r | grep "ingenue\/pkg." > testing.txt

with open('testing.txt') as f:
	testing = [x.strip() for x in f.readlines()]

print(len(testing))

for branch in testing:
	print(branch)
	download = 'wget https://raw.githubusercontent.com/ingenue/hunter/{}/{}'
	move = 'mv {} {}'
	files = ['appveyor.yml', '.travis.yml']

	for file_name in files:
		# Ex. wget https://raw.githubusercontent.com/ingenue/hunter/pkg.GTest/appveyor.yml
		subprocess.check_call(download.format(branch.split('/')[1], file_name).split())

	examples_dir = open('.travis.yml').read().split('PROJECT_DIR=')[1].split()[0]
	print(examples_dir)
	for file_name in files:
		# Ex. mv appveyor.yml cmake/projects/GTest
		subprocess.check_call(move.format(file_name, examples_dir).split())
