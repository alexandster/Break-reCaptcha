import scipy
import random
import time
import scipy.interpolate
import pyautogui

# Any duration less than this is rounded to 0.0 to instantly move the mouse.
pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
# Minimal number of seconds to sleep between mouse moves.
pyautogui.MINIMUM_SLEEP = 0  # Default: 0.05
# The number of seconds to pause after EVERY public function call.
pyautogui.PAUSE = 0  # Default: 0.1

def moveTo(x2, y2, duration):
        cp = random.randint(3, 5)  # Number of control points. Must be at least 2.

        x1, y1 = pyautogui.position()  # Starting position


        # Distribute control points between start and destination evenly.
        x = scipy.linspace(x1, x2, num=cp, dtype='int')
        y = scipy.linspace(y1, y2, num=cp, dtype='int')

        # Randomise inner points a bit (+-RND at most).
        RND = 10
        xr = scipy.random.randint(-RND, RND, size=cp)
        yr = scipy.random.randint(-RND, RND, size=cp)
        xr[0] = yr[0] = xr[-1] = yr[-1] = 0
        x += xr
        y += yr

        # Approximate using Bezier spline.
        deg = random.randint(3, 5)

        degree = deg if cp > deg else cp - 1  # Degree of b-spline. 3 is recommended.
                          # Must be less than number of control points.
        tck, u = scipy.interpolate.splprep([x, y], k=degree)
        u = scipy.linspace(0, 1, num=max(pyautogui.size()))
        points = scipy.interpolate.splev(u, tck)

        # Move mouse.
        timeout = duration / len(points[0])
        for point in zip(*(i.astype(int) for i in points)):
            pyautogui.moveTo(*point)
            time.sleep(timeout)
