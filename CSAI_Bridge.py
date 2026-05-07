from usys import stdin

MAX_LINE = 270


class Feature:
    NOSE = 0
    RIGHT_EYE = 1
    LEFT_EYE = 2
    RIGHT_EAR = 3
    LEFT_EAR = 4
    RIGHT_SHOULDER = 5
    LEFT_SHOULDER = 6
    RIGHT_ELBOW = 7
    LEFT_ELBOW = 8
    RIGHT_WRIST = 9
    LEFT_WRIST = 10
    RIGHT_HIP = 11
    LEFT_HIP = 12
    RIGHT_KNEE = 13
    LEFT_KNEE = 14
    RIGHT_ANKLE = 15
    LEFT_ANKLE = 16


class AIFeatures:

    def __init__(self):
        self.person = 0
        self.xs = [0]*17
        self.ys = [0]*17
        self.n = 0
        self.class_id = 255
        self.confidence = 0
        self.scores = []

    def _to_char(self, b):
        if not b:
            return ""
        if isinstance(b, str):
            return b
        return chr(b[0])

    def _read_frame(self):
        while True:
            ch = self._to_char(stdin.buffer.read(1))
            if ch == "P":
                break

        buf = "P"

        while len(buf) < MAX_LINE:
            ch = self._to_char(stdin.buffer.read(1))
            if not ch:
                continue
            buf += ch
            if ch == "\n":
                break

        return buf.strip()

    def update(self):
        line = self._read_frame()
        parts = line.split(",")

        if parts[0] != "P" or parts[-1] != "E":
            return False

        nums = [int(v) for v in parts[1:-1]]

        self.person = nums[0]

        self.xs = nums[1:18]
        self.ys = nums[18:35]

        self.n = nums[35]
        self.class_id = nums[36]
        self.confidence = nums[37]
        self.scores = nums[38:38+self.n]

        return True

    # -------- GETTERS --------

    def getPerson(self):
        return self.person == 1

    def getCoords(self, feature):
        return self.xs[feature], self.ys[feature]

    def getX(self, feature):
        return self.xs[feature]

    def getY(self, feature):
        return self.ys[feature]

    def getNumClasses(self):
        return self.n

    def getClassScore(self, i=None):
        if i is None:
            return self.scores
        if 0 <= i < self.n:
            return self.scores[i]
        return 0

    def getDetectedClass(self):
        return self.class_id, self.confidence