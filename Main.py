import GatherInfo, MouseMovement, time, label_image
import random

gI = GatherInfo

# Determines when the loop should stop.
stop = False

# Determines whether or not the Image needs to be clicked
check = False

# Stores the click index
# clickIndex = -1

# Saves the name.
name = 'screenShot'

# Attached to the name so that name can be reused.
nameIndex = 0

# Keeps track of the directory index.
dirIndex = 0

# Starts the driver.
gI.startDriver ("https://patrickhlauke.github.io/recaptcha/", "chrome")

# Clicks reCaptcha.
MouseMovement.moveToReCaptcha ()

MouseMovement.imageClick ()

# Makes the program wait a bit before moving on.
time.sleep (5)

matches = []

# Takes a screen shot after reCaptcha's been clicked.
matches = gI.screenShot (name + str(nameIndex), matches)
gI.incrementDirIndex ()

# Iterates nameIndex so that the same name isn't reused.
nameIndex += 1

while not stop:
	# for i in range (0, 8):
	# 	check = lI.checkImage ("./splitImage" + str (dirIndex) + "/" + str (i) + ".png")
	#
	# 	if check:
	# 		clickIndex = i
	# 		break
	# 	else:
	# 		clickIndex = -1

	# Clicks the required button.
	if len (matches) == 0:
		stop = MouseMovement.whereToClick (-1)

	random.shuffle (matches)

	for match in matches:
		stop = MouseMovement.whereToClick (match)

	# Makes the program wait a bit before moving on.
	time.sleep (6)

	# Takes a screen shot after reCaptcha's been clicked.
	matches = gI.screenShot (name + str (nameIndex), matches)
	gI.incrementDirIndex ()

	# Iterates nameIndex so that the same name isn't reused.
	nameIndex += 1

# Quits the driver.
gI.driverQuit ()