import pyautogui, random

# Saves monitor size.
x, y = pyautogui.size ()

if (x == 3840 and y == 2160):
	left = 193
	center = 376
	right = 598

	top = 382
	middle = 653
	bottom = 876

	reCaptchaX = 52
	reCaptchaY = 382

	verifyX = 590
	verifyY = 998
elif (x == 1920 and y == 1080 or x == 1920 and y == 1200):
	left = 127
	center = 259
	right = 386

	top = 300
	middle = 430
	bottom = 563

	reCaptchaX = 36
	reCaptchaY = 253

	verifyX = 403
	verifyY = 658

# Returns start reCaptcha locataion.
def startReCaptcha ():
	return randomizeMovement (reCaptchaX), randomizeMovement (reCaptchaY)

# Returns start topLeft locataion.
def topLeft ():
	return randomizeMovement (left), randomizeMovement (top)

# Returns start topCenter locataion.
def topCenter ():
	return randomizeMovement (center), randomizeMovement (top)

# Returns start topRight locataion.
def topRight ():
	return randomizeMovement (right), randomizeMovement (top)

# Returns start middleLeft locataion.
def middleLeft ():
	return randomizeMovement (left), randomizeMovement (middle)

# Returns start middleCenter locataion.
def middleCenter ():
	return randomizeMovement (center), randomizeMovement (middle)

# Returns start middleRight locataion.
def middleRight ():
	return randomizeMovement (right), randomizeMovement (middle)

# Returns start bottomLeft locataion.
def bottomLeft ():
	return randomizeMovement (left), randomizeMovement (bottom)

# Returns start bottomCenter locataion.
def bottomCenter ():
	return randomizeMovement (center), randomizeMovement (bottom)

# Returns start bottomRight locataion.
def bottomRight ():
	return randomizeMovement (right), randomizeMovement (bottom)

# Returns start verify locataion.
def verify ():
	return randomizeMovement (verifyX), randomizeMovement (verifyY)

def randomizeMovement (i):
	return i + random.randint (-17, 17)
