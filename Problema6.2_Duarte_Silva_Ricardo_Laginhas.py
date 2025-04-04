from graphics import *

class Face:
    def __init__(self, window, center, size):
        self.size = size
        self.eyeSize = 0.15 * size
        self.eyeOff = size / 3.0
        self.mouthSize = 0.8 * size
        self.mouthOff = size / 2.0
        self.center = center
        self.window = window
        self.teeth = []
        self.initializeGrimFace()

    def getCenter(self):
        return self.center

    def move(self, dx, dy):
        # Move elementos gráficos diretamente
        self.head.move(dx, dy)
        self.leftEye.move(dx, dy)
        self.rightEye.move(dx, dy)
        self.mouth.move(dx, dy)
        for tooth in self.teeth:
            tooth.move(dx, dy)
        # Atualiza a posição central
        self.center = Point(self.center.getX() + dx, self.center.getY() + dy)

    def initializeGrimFace(self):
        self.head = Circle(self.center, self.size)
        self.leftEyeOpen()
        self.rightEyeOpen()
        self.lineMouth()
        self.drawFace()

    def lineMouth(self):
        p1 = self.center.clone()
        p1.move(-self.mouthSize / 2, self.mouthOff)
        p2 = self.center.clone()
        p2.move(self.mouthSize / 2, self.mouthOff)
        self.mouth = Line(p1, p2)

    def rectMouth(self):
        p1, p2 = self.mouth.getP1(), self.mouth.getP2()
        x1, x2 = p1.getX(), p2.getX()
        y1, y2 = p1.getY(), p2.getY()
        offset = self.eyeSize / 2
        self.mouth = Rectangle(Point(x1, y1 - offset), Point(x2, y2 + offset))
        return x2, x1, y1, y2, offset

    def unDraw(self):
        self.head.undraw()
        self.leftEye.undraw()
        self.rightEye.undraw()
        self.mouth.undraw()
        for tooth in self.teeth:
            tooth.undraw()

    def drawFace(self):
        self.head.draw(self.window)
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        self.mouth.draw(self.window)
        for tooth in self.teeth:
            tooth.draw(self.window)

    def leftEyeOpen(self):
        self.leftEye = Circle(self.center, self.eyeSize)
        self.leftEye.move(-self.eyeOff, -self.eyeOff)

    def rightEyeOpen(self):
        self.rightEye = Circle(self.center, self.eyeSize)
        self.rightEye.move(self.eyeOff, -self.eyeOff)

    def leftEyeWink(self):
        center = self.leftEye.getCenter()
        x, y = center.getX(), center.getY()
        self.leftEye = Line(Point(x - self.eyeSize, y), Point(x + self.eyeSize, y))

    def rightEyeWink(self):
        center = self.rightEye.getCenter()
        x, y = center.getX(), center.getY()
        self.rightEye = Line(Point(x - self.eyeSize, y), Point(x + self.eyeSize, y))

    def wink(self):
        self.unDraw()
        self.lineMouth()
        self.leftEyeOpen()
        self.rightEyeWink()
        self.drawFace()

    def smile(self):
        self.unDraw()
        x2, x1, y1, y2, offset = self.rectMouth()
        xint = abs(x2 - x1) / 8
        self.teeth = [self.mouth]
        for i in range(8):
            t2 = Line(Point(x1 + i * xint, y1 - offset), Point((x1 + i * xint), y2 + offset))
            self.teeth.append(t2)
        self.leftEyeOpen()
        self.rightEyeOpen()
        self.drawFace()

    def meditate(self):
        self.unDraw()
        self.lineMouth()
        self.leftEyeWink()
        self.rightEyeWink()
        self.drawFace()