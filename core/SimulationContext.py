from common import *
import time
class SimulationContext:
    def __init__(self):
        self.guitoggle = True
        self.guiswitch = True
        self.frames = [framerate for _ in range(5)]
        self.etime = time.time()

        self.gmag = gmag
        self.deg = deg
        self.spinvel = spinvel
        self.bgcol = bgcol
        self.balls = []
        self.colid = 0
