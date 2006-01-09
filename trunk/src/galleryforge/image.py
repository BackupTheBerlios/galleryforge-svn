"""
  Author:     Martin Matusiak <numerodix@gmail.com>
  Program:    Creates static HTML album pages and images pages recursively
  Date:       Dec. 19, 2005

  This file is subject to the GNU General Public License (GPL)
  (http://www.gnu.org/copyleft/gpl.html)
"""

import os, glob, shutil
import Image
from logger import *
import config

class GalleryImage:
	
	filename_root = None
	thumbnail_filename = None
	
	format = None
	dim_x = 0
	dim_y = 0
	
	has_thumbnail = False
	thumbnail_suffix = None
	
	
	def __init__(self, filename_root):
		self.filename_root = filename_root

		self.readImage()
	
	
	def readImage(self):
		img = Image.open(self.filename_root)
		self.format = img.format
		(self.dim_x, self.dim_y) = img.size
		
		self.thumbnail_suffix = config.settings['thumbnail_suffix']
		(root, ext) = os.path.splitext(self.filename_root)
		self.thumbnail_filename = root + self.thumbnail_suffix + ext
		
	
	def rename(self, targetname):
		if len(glob.glob(targetname)) >= 1:
			logmw("Skipping rename for " + targetname)
			return
		
		logm("Renaming " + targetname)
		os.rename(self.filename_root, targetname)
		self.filename_root = targetname
		self.readImage()
	
	
	def hasThumbnail(self):
		if len(glob.glob(self.thumbnail_filename)) != 0:
			return True
		return False
	
	
	def makeThumbnail(self, x, y):
		if self.hasThumbnail():
			logmw("Skipping thumbnail for " + self.filename_root)
			return
		
		logm("Creating thumbnail for " + self.filename_root)
		shutil.copyfile(self.filename_root, self.thumbnail_filename)
		thumb = GalleryImage(self.thumbnail_filename)
		thumb.resize(x, y)
		
	
	def deleteThumbnail(self):
		os.remove(self.thumbnail_filename)

	
	def makeTargetSize(self, x, y):
		self.resize(x, y, qual=85)
	
	
	def resize(self, x, y, filt=Image.ANTIALIAS, aspect_ratio=True, qual=85):
		self.readImage()
		
		# keep aspect ration intact
		if aspect_ratio:
			(x, y) = self.getAspectRation(self.dim_x, self.dim_y, x, y)
			
		# dimensions are already of target size, exiting
		# also, do not enlarge images
		if (x >= self.dim_x) and (y >= self.dim_y):
			logmw("Skipping resize for " + self.filename_root)
			return
		
		logm("Resizing " + self.filename_root)
		img = Image.open(self.filename_root)
		size = (x, y)
		imgres = img.resize(size, filt)
		imgres.save(self.filename_root, quality=qual)


	def getAspectRation(self, oldx, oldy, x, y):
		oldr = float(oldx) / float(oldy)
		r = float(x) / float(y)
		
		f = 1
		if oldr > r:
			f = float(oldx) / float(x)
		else:
			f = float(oldy) / float(y)
			
		x = int(oldx / f)
		y = int(oldy / f)

		return (x, y)


