from Position import Position

class Move:
    def __init__(self,start,jump,end):
        self.start=Position(start[0],start[1])
        self.jump=Position(jump[0],jump[1])
        self.end=Position(end[0],end[1])
        self.init_params(start,jump,end);

    def init_params(self,start,jump,end):
        self.start=start
        self.jump=jump
        self.end=end

    def getStart(self):
        return self.start

    def getJump(self):
        return self.jump

    def getEnd(self):
        return self.end
