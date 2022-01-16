#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the 
   contents of the web_static folder of your AirBnB Clone repo.
   All files in the folder web_static must be added to the final archive.
   All archives must be stored in the folder versions 
   (your function should create this folder if it doesn’t exist)
   The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
"""


from fabric.api import local
import time

def do_pack():
	"""It generate a tgz archive"""
	date = time.strftime("%Y%m%d%H%M%S")
	try:
		local("mkdir -p versions")
		local("tar -czvf versions/web_static_{}.tgz web_static/".format(date))
		"""-c - instructs tar to create a new archive.
		   -z - sets the compression method to gzip.
		   -f archive-name.tgz - specifies the archive name.
		   -v option to make the tar command more visible and print the names
		   of the files being added to the archive on the terminal.
		"""
		return ("versions/web_static_{}.tgz web_static/".format(date))
	except: 
		return None
