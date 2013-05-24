import os, sys

PDTtool_path = os.path.realpath(os.path.join(os.path.realpath(__file__), '../..'))
PDTtool_subfolders = os.listdir(PDTtool_path)

for subfolder in PDTtool_subfolders:
	package = os.path.join(PDTtool_path,subfolder)
	sys.path.insert(0,package)