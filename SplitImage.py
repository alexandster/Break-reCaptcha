from pathlib import Path
import os, errno, pyautogui, label_image, MouseMovement
from PIL import Image
#from joblib import Parallel, delayed
# import multiprocessing

# Creates a name Index
nameIndex = 0

# num_cores = multiprocessing.cpu_count ()


# def processImageSplit (x, y, i, width, height, newDir):
# 	matching = []
#
# 	for j in range(0, 3):
# 		image = Image.open(dir)
#
# 		image = image.crop(
# 			((x + (j * width)), (y + (i * height)), ((x + (j * width)) + width), ((y + (i * height)) + height)))
#
# 		image.save("./" + newDir + "/" + str(nameIndex) + ".png")
#
# 		check = label_image.checkImage("./" + newDir + "/" + str(nameIndex) + ".png")
#
# 		if check:
# 			matching.append(nameIndex)
#
# 		nameIndex += 1
#
# 	return matching
#
#
# def processPartialImageSplit (match, x, y, width, height, newDir):
# 	i = j = 0
#
# 	matching = []
#
# 	if not match > 2:
# 		j = match
# 	elif not match < 3 and not match > 5:
# 		i = 1
# 		j = match - 3
# 	elif not match < 6 and not match > 8:
# 		i = 2
# 		j = match - 6
#
# 	image = Image.open(dir)
#
# 	image = image.crop(
# 		((x + (j * width)), (y + (i * height)), ((x + (j * width)) + width), ((y + (i * height)) + height)))
#
# 	image.save("./" + newDir + "/" + str(match) + ".png")
#
# 	check = label_image.checkImage("./" + newDir + "/" + str(match) + ".png")
#
# 	if check:
# 		matching.append(match)
#
# 	return matching
#
#
# def checkImages (image):
# 	return label_image.checkImage (image)


def splitImage (newDir, imgToSplit, imgToSplitDir, oldMatchLocations):
	"""

	:type newDir: The name of the new directory.
	:type imgToSplit: The name of the image that needs to be cropped.
	:type imgToSplitDir: The name of the directory of the image that needs to be cropped.
	:type oldMatchLocations: The previous match locations.
	"""
	global nameIndex
	xS, yS = pyautogui.size ()

	if xS == 3840 and yS == 2160:
		x = 101
		y = 208
		width = 189 + 6
		height = 189 + 6
	elif xS == 1920 and yS == 1080 or xS == 1920 and yS == 1200:
		x = 67
		y = 138
		width = 126 + 4
		height = 126 + 4

	if not os.path.exists (newDir):
		try:
			os.mkdir (newDir)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise

		print ("Path created")
	else:
		print ("Path already exists")

	dir = "./" + imgToSplitDir + "/" + imgToSplit + ".png"

	matches = []

	nameIndex = 0

	# pool = multiprocessing.Pool ()
	# manager = multiprocessing.Manager ()

	# images = []

	checks = []

	if len (oldMatchLocations) == 0:
		for i in range (0, 3):
			nameIndex = 3 * i

			image = Image.open (dir)

			image = image.crop(
				(x, (y + (i * height)), x + (3 * width), ((y + (i * height)) + height)))

			image.save("./" + newDir + "/" + str (nameIndex) + "Big" + ".png")

			check = label_image.checkColumn ("./" + newDir + "/" + str (nameIndex) + "Big" + ".png")

			if check:
				for j in range (0, 3):
					image = Image.open(dir)

					MouseMovement.whereToMove(nameIndex)

					image = image.crop(
						((x + (j * width)), (y + (i * height)), ((x + (j * width)) + width),
						 ((y + (i * height)) + height)))

					image.save("./" + newDir + "/" + str(nameIndex) + ".png")

					check = label_image.checkImage("./" + newDir + "/" + str(nameIndex) + ".png")

					if check:
						matches.append(nameIndex)

					nameIndex += 1

		# i represents columns j represents row
		# for i in range (0, 3):
		# 	for j in range (0, 3):
		# 		image = Image.open (dir)
		#
		# 		MouseMovement.whereToMove (nameIndex)
		#
		# 		image = image.crop (
		# 			((x + (j * width)), (y + (i * height)), ((x + (j * width)) + width), ((y + (i * height)) + height)))
		#
		# 		# images.append (image)
		#
		# 		image.save ("./" + newDir + "/" + str (nameIndex) + ".png")
		#
		# 		check = label_image.checkImage ("./" + newDir + "/" + str (nameIndex) + ".png")
		#
		# 		if check:
		# 			matches.append (nameIndex)
		# 		# 	MouseMovement.imageClick ()
		#
				# nameIndex += 1
	else:
		for match in oldMatchLocations:
			i = j = 0

			if not match > 2:
				j = match
			elif not match < 3 and not match > 5:
				i = 1
				j = match - 3
			elif not match < 6 and not match > 8:
				i = 2
				j = match - 6

			image = Image.open (dir)

			MouseMovement.whereToMove (match)

			image = image.crop (
				((x + (j * width)), (y + (i * height)), ((x + (j * width)) + width), ((y + (i * height)) + height)))

			image.save ("./" + newDir + "/" + str (match) + ".png")

			check = label_image.checkImage ("./" + newDir + "/" + str (match) + ".png")

			if check:
				matches.append (match)
				# MouseMovement.imageClick ()

			nameIndex += 1

	# checks.append (pool.map (checkImages, images))
	# pool.close ()
	# pool.terminate ()
	# pool.join ()
	#
	# matches = [i for i, c in checks if c]

	# if len (oldMatchLocations) == 0:
		# matches.append (Parallel (n_jobs = num_cores)(delayed (processImageSplit)(x, y, i, width, height, newDir) for i in range (0, 3)))
	# else:
		# matches.append (Parallel (n_jobs = num_cores)(delayed (processPartialImageSplit)(match, x, y, width, height, newDir) for match in oldMatchLocations))

	return matches