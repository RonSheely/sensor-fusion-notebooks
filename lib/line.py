# Michael P. Hayes UCECE, Copyright 2018--2019

import numpy as np

class Line(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    @property
    def A(self):
        return self.p1[1] - self.p2[1]
    
    @property
    def B(self):        
        return self.p2[0] - self.p1[0]
    
    @property
    def C(self):
        return self.p2[0] * self.p1[1] - self.p1[0] * self.p2[1]
    
    def intersection(self, line):
        
        if not isinstance(line, Line):
            line = Line(*line)
            
        D  = self.A * line.B - self.B * line.A
        Dx = self.C * line.B - self.B * line.C
        Dy = self.A * line.C - self.C * line.A
        
        if D == 0:
            return False
        x = Dx / D
        y = Dy / D
        return x, y

    def coord(self, t):

        x = self.p1[0] + t * (self.p2[0] - self.p1[0])
        y = self.p1[1] + t * (self.p2[1] - self.p1[1])
        return x, y

    
class LineSeg(Line):

    def intersection(self, lineseg):
        R = super(LineSeg, self).intersection(lineseg)
        if not R:
            return False
        x, y = R

        if self.p2[0] != self.p1[0]:
            t = (x - self.p1[0]) / (self.p2[0] - self.p1[0])
        else:
            t = (y - self.p1[1]) / (self.p2[1] - self.p1[1])            
        if t > 1 or t < 0:
            return False

        if lineseg.p2[0] != lineseg.p1[0]:
            t = (x - lineseg.p1[0]) / (lineseg.p2[0] - lineseg.p1[0])
        else:
            t = (y - lineseg.p1[1]) / (lineseg.p2[1] - lineseg.p1[1])
        if t > 1 or t < 0:
            return False
        
        return R

    @property
    def length(self):

        return np.sqrt((self.p2[0] - self.p1[0])**2 +
                       (self.p2[1] - self.p1[1])**2)
    
