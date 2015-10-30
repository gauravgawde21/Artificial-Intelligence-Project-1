__author__ = 'gp'
class Moves:

    def __init__(self):
        #1
        self.possMoves={((0,2),(0,3),(0,4)), ((0,2),(1,2),(2,2))}
        self.validMoves = dict({(0,2): self.possMoves})

        self.possCost={((10),(10))};
        self.validCost=dict({(0,2):self.possCost})

        self.possHeuristic1={((5),(3))};
        self.validHeuristic1=dict({(0,2):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2=dict({(0,2):self.possHeuristic2})

        #2
        self.possMoves={((0,3),(1,3),(2,3))}
        self.validMoves.update({(0,3): self.possMoves})

        self.possCost={((10))};
        self.validCost.update({(0,3):self.possCost})

        self.possHeuristic1={((1))};
        self.validHeuristic1.update({(0,3):self.possHeuristic1})

        self.possHeuristic2={((0))};
        self.validHeuristic2.update({(0,3):self.possHeuristic2})

        #3
        self.possMoves={((0,4),(0,3),(0,2)),((0,4),(1,4),(2,4))}
        self.validMoves.update({(0,4):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(0,4):self.possCost})

        self.possHeuristic1={((5),(3))};
        self.validHeuristic1.update({(0,4):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(0,4):self.possHeuristic2})

        #4
        self.possMoves={((1,2),(2,2),(3,2)),((1,2),(1,3),(1,4))}
        self.validMoves.update({(1,2):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(1,2):self.possCost})

        self.possHeuristic1={((1),(4))};
        self.validHeuristic1.update({(1,2):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(1,2):self.possHeuristic2})


        #5
        self.possMoves={((1,3),(2,3),(3,3))}
        self.validMoves.update({(1,3):self.possMoves})

        self.possCost={((10))};
        self.validCost.update({(1,3):self.possCost})

        self.possHeuristic1={(0)};
        self.validHeuristic1.update({(1,3):self.possHeuristic1})

        self.possHeuristic2={(0)};
        self.validHeuristic2.update({(1,3):self.possHeuristic2})

        #6
        self.possMoves={((1,4),(1,3),(1,2)),((1,4),(2,4),(3,4))}
        self.validMoves.update({(1,4):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(1,4):self.possCost})

        self.possHeuristic1={((4),(1))};
        self.validHeuristic1.update({(1,4):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(1,4):self.possHeuristic2})

        #7
        self.possMoves={((2,0),(3,0),(4,0)),((2,0),(2,1),(2,2))}
        self.validMoves.update({(2,0):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(2,0):self.possCost})

        self.possHeuristic1={((5),(3))};
        self.validHeuristic1.update({(2,0):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(2,0):self.possHeuristic2})


        #8
        self.possMoves={((2,1),(3,1),(4,1)),((2,1),(2,2),(2,3))}
        self.validMoves.update({(2,1):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(2,1):self.possCost})

        self.possHeuristic1={((4),(1))};
        self.validHeuristic1.update({(2,1):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(2,1):self.possHeuristic2})

        #9
        self.possMoves={((2,2),(2,1),(2,0)),((2,2),(1,2),(0,2)),((2,2),(2,3),(2,4)),((2,2),(3,2),(4,2))}
        self.validMoves.update({(2,2):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(2,2):self.possCost})

        self.possHeuristic1={((5),(5),(2),(3))};
        self.validHeuristic1.update({(2,2):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(2,2):self.possHeuristic2})

        #10
        self.possMoves={((2,3),(2,2),(2,1)),((2,3),(2,4),(2,5)),((2,3),(3,3),(4,3)),((2,3),(1,3),(0,3))}
        self.validMoves.update({(2,3):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(2,3):self.possCost})

        self.possHeuristic1={((4),(4),(1),(4))};
        self.validHeuristic1.update({(2,3):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(2,3):self.possHeuristic2})

        #11
        self.possMoves={((2,4),(2,3),(2,2)),((2,4),(2,5),(2,6)),((2,4),(3,4),(4,4)),((2,4),(2,3),(2,2))}
        self.validMoves.update({(2,4):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(2,4):self.possCost})

        self.possHeuristic1={((3),(5),(3),(3))};
        self.validHeuristic1.update({(2,4):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(2,4):self.possHeuristic2})

        #12
        self.possMoves={((2,5),(2,4),(2,3)),((2,5),(3,5),(4,5))}
        self.validMoves.update({(2,5):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(2,5):self.possCost})

        self.possHeuristic1={((1),(4))};
        self.validHeuristic1.update({(2,5):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(2,5):self.possHeuristic2})

        #13
        self.possMoves={((2,6),(2,5),(2,4)),((2,6),(3,6),(4,6))}
        self.validMoves.update({(2,6):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(2,6):self.possCost})

        self.possHeuristic1={((2),(5))};
        self.validHeuristic1.update({(2,6):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(2,6):self.possHeuristic2})

        #33
        self.possMoves={((3,0),(3,1),(3,2))}
        self.validMoves.update({(3,0):self.possMoves})

        self.possCost={((10))};
        self.validCost.update({(3,0):self.possCost})

        self.possHeuristic1={((1))};
        self.validHeuristic1.update({(3,0):self.possHeuristic1})

        self.possHeuristic2={((0))};
        self.validHeuristic2.update({(3,0):self.possHeuristic2})

        #14
        self.possMoves={((3,1),(3,2),(3,3))}
        self.validMoves.update({(3,1):self.possMoves})

        self.possCost={((10))};
        self.validCost.update({(3,1):self.possCost})

        self.possHeuristic1={((0))};
        self.validHeuristic1.update({(3,1):self.possHeuristic1})

        self.possHeuristic2={((0))};
        self.validHeuristic2.update({(3,1):self.possHeuristic2})

        #15
        self.possMoves={((3,2),(3,1),(3,0)),((3,2),(2,2),(1,2)),((3,2),(3,3),(3,4)),((3,2),(4,2),(5,2))}
        self.validMoves.update({(3,2):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(3,2):self.possCost})

        self.possHeuristic1={((4),(4),(1),(4))};
        self.validHeuristic1.update({(3,2):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(3,2):self.possHeuristic2})

        #16
        self.possMoves={((3,3),(3,2),(3,1)),((3,3),(2,3),(1,3)),((3,3),(3,4),(3,5)),((3,3),(4,3),(5,3))}
        self.validMoves.update({(3,3):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(3,3):self.possCost})

        self.possHeuristic1={((3),(3),(3),(3))};
        self.validHeuristic1.update({(3,3):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(3,3):self.possHeuristic2})

        #17
        self.possMoves={((3,4),(3,3),(3,2)),((3,4),(3,5),(3,6)),((3,4),(2,4),(1,4)),((3,4),(4,4),(5,4))}
        self.validMoves.update({(3,4):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(3,4):self.possCost})

        self.possHeuristic1={((1),(4),(4),(4))};
        self.validHeuristic1.update({(3,4):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(3,4):self.possHeuristic2})

        #18
        self.possMoves={((3,5),(3,4),(3,3))}
        self.validMoves.update({(3,5):self.possMoves})

        self.possCost={((10))};
        self.validCost.update({(3,5):self.possCost})

        self.possHeuristic1={((0))};
        self.validHeuristic1.update({(3,5):self.possHeuristic1})

        self.possHeuristic2={((0))};
        self.validHeuristic2.update({(3,5):self.possHeuristic2})

        #19
        self.possMoves={((3,6),(3,5),(3,4))}
        self.validMoves.update({(3,6):self.possMoves})

        self.possCost={((10))};
        self.validCost.update({(3,6):self.possCost})

        self.possHeuristic1={((1))};
        self.validHeuristic1.update({(3,6):self.possHeuristic1})

        self.possHeuristic2={((0))};
        self.validHeuristic2.update({(3,6):self.possHeuristic2})

        #20
        self.possMoves={((4,0),(3,0),(2,0)),((4,0),(4,1),(4,2))}
        self.validMoves.update({(4,0):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(4,0):self.possCost})

        self.possHeuristic1={((5),(3))};
        self.validHeuristic1.update({(4,0):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(4,0):self.possHeuristic2})

        #21
        self.possMoves={((4,1),(3,1),(2,1)),((4,1),(4,2),(4,3))}
        self.validMoves.update({(4,1):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(4,1):self.possCost})

        self.possHeuristic1={((4),(1))};
        self.validHeuristic1.update({(4,1):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(4,1):self.possHeuristic2})

        #22
        self.possMoves={((4,2),(4,1),(4,0)),((4,2),(3,2),(2,2)),((4,2),(5,2),(5,2)),((4,2),(4,3),(4,4))}
        self.validMoves.update({(4,2):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(4,2):self.possCost})

        self.possHeuristic1={((5),(3),(4),(3))};
        self.validHeuristic1.update({(4,2):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(4,2):self.possHeuristic2})

        #23
        self.possMoves={((4,3),(4,2),(4,1)),((4,3),(3,3),(2,3)),((4,3),(4,4),(4,5)),((4,3),(5,3),(6,3))}
        self.validMoves.update({(4,3):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(4,3):self.possCost})

        self.possHeuristic1={((4),(1),(4),(4))};
        self.validHeuristic1.update({(4,3):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(4,3):self.possHeuristic2})

        #24
        self.possMoves={((4,4),(4,3),(4,2)),((4,4),(3,4),(2,4)),((4,4),(4,5),(4,6)),((4,4),(5,4),(6,4))}
        self.validMoves.update({(4,4):self.possMoves})

        self.possCost={((10),(10),(10),(10))};
        self.validCost.update({(4,4):self.possCost})

        self.possHeuristic1={((3),(3),(5),(5))};
        self.validHeuristic1.update({(4,4):self.possHeuristic1})

        self.possHeuristic2={((0),(0),(0),(0))};
        self.validHeuristic2.update({(4,4):self.possHeuristic2})

        #25
        self.possMoves={((4,5),(4,4),(4,3)),((4,5),(3,5),(2,5))}
        self.validMoves.update({(4,5):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(4,5):self.possCost})

        self.possHeuristic1={((1),(4))};
        self.validHeuristic1.update({(4,5):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(4,5):self.possHeuristic2})

        #26
        self.possMoves={((4,6),(4,5),(4,4)),((4,6),(3,6),(2,6))}
        self.validMoves.update({(4,6):self.possMoves})

        #27
        self.possMoves={((5,2),(4,2),(3,2)),((5,2),(5,3),(5,4))}
        self.validMoves.update({(5,2):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(5,2):self.possCost})

        self.possHeuristic1={((1),(4))};
        self.validHeuristic1.update({(5,2):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(5,2):self.possHeuristic2})

        #28
        self.possMoves={((5,3),(4,3),(2,3))}
        self.validMoves.update({(5,3):self.possMoves})

        self.possCost={((10))};
        self.validCost.update({(5,3):self.possCost})

        self.possHeuristic1={((1))};
        self.validHeuristic1.update({(5,3):self.possHeuristic1})

        self.possHeuristic2={((0))};
        self.validHeuristic2.update({(5,3):self.possHeuristic2})

        #29
        self.possMoves={((5,4),(4,4),(3,4)),((5,4),(5,3),(5,2))}
        self.validMoves.update({(5,4):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(5,4):self.possCost})

        self.possHeuristic1={((1),(4))};
        self.validHeuristic1.update({(5,4):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(5,4):self.possHeuristic2})

        #30
        self.possMoves={((6,2),(5,2),(4,2)),((6,2),(6,3),(6,4))}
        self.validMoves.update({(6,2):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(6,2):self.possCost})

        self.possHeuristic1={((3),(5))};
        self.validHeuristic1.update({(6,2):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(6,2):self.possHeuristic2})

        #31
        self.possMoves={((6,3),(5,3),(4,3))}
        self.validMoves.update({(6,3):self.possMoves})

        self.possCost={((10))};
        self.validCost.update({(6,3):self.possCost})

        self.possHeuristic1={((1))};
        self.validHeuristic1.update({(6,3):self.possHeuristic1})

        self.possHeuristic2={((0))};
        self.validHeuristic2.update({(6,3):self.possHeuristic2})

        #32
        self.possMoves={((6,4),(6,3),(6,2)),((6,4),(5,4),(4,4))}
        self.validMoves.update({(6,4):self.possMoves})

        self.possCost={((10),(10))};
        self.validCost.update({(6,4):self.possCost})

        self.possHeuristic1={((5),(3))};
        self.validHeuristic1.update({(6,4):self.possHeuristic1})

        self.possHeuristic2={((0),(0))};
        self.validHeuristic2.update({(6,4):self.possHeuristic2})

        #print self.validMoves
        #print self.validMoves[(6,4)]
        #print self.validCost[(6,4)]
        #print self.validHeuristic1[(6,4)]
        #print self.validHeuristic2[(6,4)]

        #print self.validHeuristic1
        #print self.validHeuristic2

    def getMoves(self,position):
        #print "Position Values::",position.row,position.col;
        return self.validMoves[(position.row,position.col)]

    def getCost(self,position):
        return self.validCost[(position.row,position.col)]

    def getHeuristic1(self,position):
        return self.validHeuristic1[(position.row,position.col)]

    def getHeuristic2(self,position):
        return self.validHeuristic2[(position.row,position.col)]

moves_obj=Moves();
