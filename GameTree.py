from GameBoard import GameBoard

class GameTree:
    def __init__(self,gb_obj):
        self.level=None;
        self.gb=None;
        self.children=[""];
        self.InitGameTree(gb_obj);
        self.children.remove("");

    def InitGameTree(self,gb):
        self.gb=gb;

    def addChild(self,child):
        self.children.append(child);

    def getGameBoard(self):
        return self.gb;

    def has_children(self):
        return len(self.children)>0

    def getFirstChild(self):
        return self.children[0];

    def num_children(self):
        return len(self.children);

    def removeFirstChild(self):
        self.children.remove(self.children[0]);

