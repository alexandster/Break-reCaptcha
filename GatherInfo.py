from selenium import webdriver
from pathlib import Path
import os, errno, SplitImage

# Initializes driver.
driver = None

sI = SplitImage

# Checks to see if the driver has started.
# If the driver hasn't started you shouldn't
# be able to take a screen shot or quit the
# driver.
started = False

directory = 'screenShots'

dirIndex = 0

matches = []

# Starts the driver up with the requested webdriver
# and sets the requested url.
def startDriver (url, webDrive):
	global driver
	
	if (not getStarted ()):
		if (webDrive == "chrome"):
			driver = webdriver.Chrome ('Drivers/chromedriver.exe')
		elif (webDrive == "opera"):
			driver = webdriver.Opera ('Drivers/operadriver.exe')
		else:
			driver = webdriver.PhantomJS ('Drivers/phantomjs.exe')

		driver.maximize_window ()
		driver.set_page_load_timeout (30)
		driver.implicitly_wait (20)
		
		driver.get (url)

		_setStartedTrue ()
	else:
		print ("The driver has already been started and you can't start it again.")


# Saves a screen shot of the web page under the
# requested file name.
def screenShot (fileName, oldMatchLocations):
	global driver, dirIndex

	if (getStarted ()):
		if (not os.path.exists (directory)):
			try:
				os.mkdir (directory)
			except OSError as e:
				if e.errno != errno.EEXIST:
					raise

			print ("Path created")
		else:
			print ("Path already exists")

		myFile = Path ("./screenShots/" + fileName + ".png")
		
		if (myFile.exists ()):
			print (fileName + ".png " + "exists")
		else:
			driver.get_screenshot_as_file ("./screenShots/" + fileName + ".png")

		dirName = "splitImage" + str (dirIndex)

		matches = sI.splitImage (dirName, fileName, "screenShots", oldMatchLocations)
	else:
		print ("The driver hasn't started yet, please start it first")

	return matches

# Increments dirIndex.
def incrementDirIndex ():
	global dirIndex

	dirIndex += 1

# Quits the driver.
def driverQuit ():
	global driver
	
	if (getStarted ()):
		driver.quit ()
		_setStartedFalse ()
	else:
		print ("Can't stop a driver that hasn't been started")


# Sets started to false.
def _setStartedFalse ():
	global started
	started = False


# Sets started to true
def _setStartedTrue ():
	global started
	started = True


# Returns started value.
def getStarted ():
	return started

#startDriver ("https://patrickhlauke.github.io/recaptcha/", "chrome")