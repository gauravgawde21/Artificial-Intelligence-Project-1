from GameBoard import GameBoard;
from GameTree import GameTree;
from Position import Position;
import sys;

class Play:
    def __init__(self):
        self.startBoard = None
        self.init_GameBoard();

    def init_GameBoard(self):
        #print "In init_GameBoard() of Play Class";

        #Calls constructor of GameBoard Class
        self.startBoard = GameBoard();

    def dfs(self):
        #print "In dfs() of Play Class"

        #root node of type GameTree
        root=GameTree(self.startBoard)

        #
        possible_boards=root.getGameBoard().possibleBoards();

        #print "Possible Board Values in Play Class::",possible_boards;
        for nextBoard in possible_boards:
            nextNode=GameTree(nextBoard);
            #print "NextBoard Value in dfs() of Play Class::",nextBoard;
            if(self.play(nextBoard,nextNode)):
                root.addChild(nextNode);

    def play(self,gb,parent):
        node_counter=0;
        if(gb.finalBoard()):
            found=True;
        else:
            found=False;
            nextBoards=gb.possibleBoards();
            #print "NextBoard Values in Play Class::",nextBoards;
            for nextBoard in nextBoards:
                nextNode=GameTree(nextBoard)
                if(self.play(nextBoard,nextNode)):
                    node_counter=node_counter+1
                    parent.addChild(nextNode)
        print "Number Of Nodes Expanded::",node_counter
        return found

    def iddfs(self):
        root=GameTree(self.startBoard);
        depth_val=0;
        ret_val=False;
        #every time initial configuration and hence infinite loop
        #possible_boards=self.startBoard.possibleBoards();
        #false value so run again
        #true value so stop
        while(not(ret_val)):
            #print "In while loop with depth::",depth_val
            ret_val = self.depth_ls(root,depth_val,self.startBoard);
            #Increase depth after each iteration
            depth_val=depth_val+1;

    def depth_ls(self,parent,depth_val,gb):
        if(depth_val>=0):
            #print "depth_val>=0::",depth_val>=0
            nextBoards=gb.possibleBoards();
            #print "nextBoard::",nextBoards

            for nextBoard in nextBoards:

                nextNode=GameTree(nextBoard);

                if(self.depth_ls(nextNode,depth_val-1,nextBoard)):
                    parent.addChild(nextNode)

                #early detection for final board
                if(nextBoard.finalBoard()):
                    return True
        else:
            #print "depth_val>=0",depth_val>=0
            #invalid depth lookup so return
            #print "Accessing nodes at invalid depth so returing::"
            return False;


    #1--First heuristic
    #2--Second heuristic

    def astar(self,heuristic_val):
            #print "In dfs() of Play Class"

        #root node of type GameTree
        root=GameTree(self.startBoard)

        #Expand Boards Based On The The Heuristics
        possible_boards=root.getGameBoard().possibleBoards();

        #print "Possible Board Values in Play Class::",possible_boards;
        for nextBoard in possible_boards:
            nextNode=GameTree(nextBoard);
            #print "NextBoard Value in dfs() of Play Class::",nextBoard;
            if(self.play(nextBoard,nextNode)):
                root.addChild(nextNode);





