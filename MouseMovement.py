import ClickLocations, scipy, HumanMove
import pyautogui

d = 1

# Moves to reCaptcha.
def moveToReCaptcha ():
	x, y = ClickLocations.startReCaptcha ()

	HumanMove.moveTo (x, y, duration = d)

# Moves to top-left.
def moveToTopLeft ():
	x, y = ClickLocations.topLeft ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to top-center.
def moveToTopCenter ():
	x, y = ClickLocations.topCenter ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to top-right.
def moveToTopRight ():
	x, y = ClickLocations.topRight ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to middle-left.
def moveToMiddleLeft ():
	x, y = ClickLocations.middleLeft ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to middle-center.
def moveToMiddleCenter ():
	x, y = ClickLocations.middleCenter ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to middle-right.
def moveToMiddleRight ():
	x, y = ClickLocations.middleRight ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to bottom-left.
def moveToBottomLeft ():
	x, y = ClickLocations.bottomLeft ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to bottom-center.
def moveToBottomCenter ():
	x, y = ClickLocations.bottomCenter ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to bottom-right.
def moveToBottomRight ():
	x, y = ClickLocations.bottomRight ()

	HumanMove.moveTo (x, y, duration = d)


# Moves to verify.
def moveToVerify ():
	x, y = ClickLocations.verify ()

	HumanMove.moveTo (x, y, duration = d)


# Clicks the image.
def imageClick ():
	pyautogui.click ()


def whereToMove (moveTo):
	if moveTo == 0:
		moveToTopLeft ()
	elif moveTo == 1:
		moveToTopCenter ()
	elif moveTo == 2:
		moveToTopRight ()
	elif moveTo == 3:
		moveToMiddleLeft ()
	elif moveTo == 4:
		moveToMiddleCenter ()
	elif moveTo == 5:
		moveToMiddleRight ()
	elif moveTo == 6:
		moveToBottomLeft ()
	elif moveTo == 7:
		moveToBottomCenter ()
	elif moveTo == 8:
		moveToBottomRight()


def whereToClick (click):
	if click == -1:
		moveToVerify ()

		imageClick ()

		return True
	elif click == 0:
		moveToTopLeft ()

		imageClick ()
	elif click == 1:
		moveToTopCenter ()

		imageClick ()
	elif click == 2:
		moveToTopRight ()

		imageClick ()
	elif click == 3:
		moveToMiddleLeft ()

		imageClick ()
	elif click == 4:
		moveToMiddleCenter ()

		imageClick ()
	elif click == 5:
		moveToMiddleRight ()

		imageClick ()
	elif click == 6:
		moveToBottomLeft ()

		imageClick ()
	elif click == 7:
		moveToBottomCenter ()

		imageClick ()
	elif click == 8:
		moveToBottomRight()

		imageClick ()