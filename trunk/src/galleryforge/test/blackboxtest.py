#!/usr/bin/python

"""
  Author:     Martin Matusiak <numerodix@gmail.com>
  Program:    Creates static HTML album pages and images pages recursively
  Date:       Dec. 19, 2005

  This file is subject to the GNU General Public License (GPL)
  (http://www.gnu.org/copyleft/gpl.html)
"""

import sys, shutil
sys.path.append("..")

import launch
import config
from testhelper import *
from logger import *
import unittest, glob, time


class BlackBoxTest(unittest.TestCase):
	
	loc = "gallery/cat/subcat/subsubcat/album"
	loc2 = "gallery/cat/subcat2/subsubcat/album"
	loc3 = "gallery/cat/subcat/subsubcat2/album"
	loc4 = "gallery/cat2/subcat/subsubcat2/album"
	
	absloc = os.path.abspath("gallery")
	
	imfile = "img.jpg"
	path = os.path.abspath(os.path.join(loc, imfile))

	
	def setUp(self):
		makeQuiet()
		if os.path.exists(self.absloc):
			shutil.rmtree(self.absloc)
		
	
	def tearDown(self):
		if os.path.exists(self.absloc):
			pass
			#shutil.rmtree(self.absloc)
	
	
	def testNoClobber(self):
		"""testNoClobber: don't overwrite images from a previous run"""
		itfile = "0001.jpg"
		tpath = os.path.abspath(os.path.join(self.loc, itfile))

		os.makedirs(self.loc)
		createDummyImage(self.path)
		
		launch.main(basepath=self.absloc)
		
		odate = os.path.getmtime(tpath)
		
		launch.main(basepath=self.absloc)
		
		ndate = os.path.getmtime(tpath)
		
		self.assertEqual(odate, ndate)
		
		shutil.rmtree(self.absloc)


	def testScanDirs(self):
		"""testScanDirs: process [only] all directories with images"""
		for i in self.loc, self.loc2, self.loc3, self.loc4:
			abspath = os.path.abspath(i)
			os.makedirs(abspath)
			imfile = os.path.join(i, self.imfile)
			
			if not i == self.loc3:
				createDummyImage(imfile)
		
		launch.main(basepath=self.absloc)
		
		for i in self.loc, self.loc2, self.loc3, self.loc4:
			abspath = os.path.abspath(i)
			files = glob.glob(os.path.join(abspath, "*"))
			
			if i == self.loc3:
				self.assertEqual(len(files), 0)
			else:
				search_for = ["0001.jpg", "0001_thumb.jpg", "0001.html",
					"a0001.html", "index.php", config.settings['dummyimg']]
				for f in search_for:
					absfile = os.path.join(abspath, f)
					self.assertTrue(absfile in files)
				
		shutil.rmtree(self.absloc)


	def testRebuildThumbnails(self):
		"""testRebuildThumbnails: thumbnails should be rebuilt (broken on win32)"""
			
		absdest = os.path.abspath(self.loc)
		os.makedirs(absdest)
		
		for i in "img.jpg", "img2.jpg", "img3.jpg":
			afile = os.path.join(absdest, i)
			createDummyImage(afile)
		
		launch.main(basepath=self.absloc)
		
		dates = {}
		for i in "0001_thumb.jpg", "0002_thumb.jpg", "0003_thumb.jpg":
			afile = os.path.join(absdest, i)
			
			dates[i] = os.path.getmtime(afile)
		
		tpre = time.strftime("%S", time.gmtime())
		time.sleep(1)		# make sure they are not created too soon
		tpost = time.strftime("%S", time.gmtime())
		self.assertNotEqual(tpre, tpost)	# if test fails, should always be here
		
		config.settings['rebuild_thumbnails'] = True
		config.store(config.settings)
		
		launch.main(basepath=self.absloc, rebuild_thumbnails=True)
		
		config.settings['rebuild_thumbnails'] = False
		config.store(config.settings)
		
		for i in "0001_thumb.jpg", "0002_thumb.jpg", "0003_thumb.jpg":
			afile = os.path.join(absdest, i)
			cdate = os.path.getmtime(afile)
			self.assertNotEqual(dates[i], cdate)
		
		shutil.rmtree(self.absloc)


	def testCheckIndex(self):
		"""testCheckIndex: index file should be well formed"""
		indexfile = os.path.join(self.absloc, "index")
		
		for i in self.loc, self.loc2, self.loc3, self.loc4:
			abspath = os.path.abspath(i)
			os.makedirs(abspath)
			imfile = os.path.join(i, self.imfile)
			createDummyImage(imfile)
		
		launch.main(basepath=self.absloc)
		
		self.assertTrue(os.path.exists(indexfile))
		
		tmp = open(indexfile, 'r')
		lines = []
		for line in tmp.xreadlines():
			lines.append(line)
		tmp.close()
		
		for line in lines:
			parts = line.split(",")
			path = os.path.join(self.absloc, parts[2])
			self.assertTrue(path)
		
		shutil.rmtree(self.absloc)




def run(verbosity=1):
	suite = unittest.makeSuite(BlackBoxTest)
	unittest.TextTestRunner(verbosity=verbosity).run(suite)


if __name__ == "__main__":
	run()
