import copy
from Position import Position
from Moves import Moves
from Move import Move
import sys
import time


class GameBoard:
    def __init__(self):
        #print "In GameBoard Constructor"
        # Creates a list containing 5 lists initialized to 0
        self.start_time = time.time()
        self.pins = [[0 for x in range(7)] for x in range(7)]
        self.locations=[[0 for x in range(7)] for x in range(7)]
        self.c=[[0 for x in range(7)] for x in range(7)]
        self.h1=[[0 for x in range(7)] for x in range(7)]
        self.h2=[[0 for x in range(7)] for x in range(7)]
        self.f=[[0 for x in range(7)] for x in range(7)]

        #Step 1:Specify holes
        for i in range(0,7):
            for j in range(0,7):
                self.pins[i][j]="0"

        #Step 2:Ignore
        self.pins[0][0]="-";
        self.pins[0][1]="-";
        self.pins[1][0]="-";
        self.pins[1][1]="-";
        self.pins[0][5]="-";
        self.pins[0][6]="-";
        self.pins[1][5]="-";
        self.pins[1][6]="-";
        self.pins[5][0]="-";
        self.pins[5][1]="-";
        self.pins[6][0]="-";
        self.pins[6][1]="-";
        self.pins[5][5]="-";
        self.pins[5][6]="-";
        self.pins[6][5]="-";
        self.pins[6][6]="-";

        #Step 3:Pegs
        #self.pins[0][3]="X";
        self.pins[1][3]="X";
        self.pins[2][3]="X";
        self.pins[2][2]="X";
        self.pins[2][4]="X";
        self.pins[3][3]="X";
        self.pins[4][3]="X";
        #self.pins[3][2]="X";
        #self.pins[3][4]="X";

        #print self.pins;
        #exit("constructor exit");
        #print self.pins

        #Initialize location array
        counter=0
        for i in range(0,7):
            for j in range(0,7):
                if(self.pins[i][j]!="-"):
                    self.locations[i][j]=counter;
                    counter=counter+1

        #Print Location Array
        #for loc_val in self.locations:
            #print loc_val

    def GameBoard(self,game_obj):
        for i in range(0,7):
            for j in range(0,7):
                self.pins[i][j]=game_obj[i][j];

    def possibleBoards(self):
        #List Object
        boards=[""]
        for i in range(0,7):
            for j in range(0,7):
                if(self.pins[i][j]!="-" and self.pins[i][j]!="0"):

                    #Position object specifies row and col
                    start = Position(i,j)

                    #Moves object specifies start,jump and end
                    moves_obj=Moves()

                    #Read all possible moves of a particular point(x,y) from dictionary
                    possible_moves=moves_obj.getMoves(start);

                    #print "Possible Moves::",possible_moves;
                    #print "==========================================================="
                    for move_point in possible_moves:
                        #move_point[0]:start,jump and end
                        move=Move(move_point[0],move_point[1],move_point[2]);

                        #print "Individual Move::",move_loop;
                        if(self.validMove(move)):
                            boards.append(self.jump(move))

        #remove first item from list array which is empty string
        boards.remove("");

        #print "Board Values in PossibleBoards()::",boards;
        #exit("exit exit");
        return boards;


    def astar_possibleBoards(self,heuristic_val):
        #List Object
        boards=[""]
        for i in range(0,7):
            for j in range(0,7):
                if(self.pins[i][j]!="-" and self.pins[i][j]!="0"):
                    #Position object specifies row and col

                    start = Position(i,j)

                    #Moves object specifies start,jump and end
                    moves_obj=Moves()

                    #Read all possible moves of a particular point(x,y) from dictionary
                    possible_moves=moves_obj.getMoves(start);


                    #Read all possible costs related to a particular move
                    possible_costs=moves_obj.getCost(start);

                    #Read all heuristics related to a particular move
                    if(heuristic_val==1):
                        possible_heuristics=moves_obj.getHeuristic1(start);
                    else:
                        possible_heuristics=moves_obj.getHeuristic2(start);

                    #code for finding fn from hn and gn values
                    if(heuristic_val==1):
                        for i in range(0,7):
                            for j in range(0,7):
                                self.f[i][j]=self.c[i][j]+self.h1[i][j];
                    if(heuristic_val==2):
                        for i in range(0,7):
                            for j in range(0,7):
                                self.f[i][j]=self.c[i][j]+self.h2[i][j];

                        for move_point in possible_moves:
                            #move_point[0]:start,jump and end

                            move=Move(move_point[0],move_point[1],move_point[2]);

                            #print "Individual Move::",move_loop;
                            if(self.validMove(move)):
                                boards.append(self.jump(move))

        #remove first item from list array which is empty string
        boards.remove("");

        #print "Board Values in PossibleBoards()::",boards;
        #exit("exit exit");
        return boards;

    def validMove(self,move):
        #Empty Start

        #print "-------------------------------------------------------";
        #print "In validMove()"
        #print "Start Position::",(move.getStart()[0]),(move.getStart()[1]);
        #print "Jump Position::",(move.getJump()[0]),(move.getJump()[1]);
        #print "End Position::",(move.getEnd()[0]),(move.getEnd()[1]);
        #print move.getStart()[0],move.getStart()[1],self.pins[move.getStart()[0]][move.getStart()[1]];
        #print move.getJump()[0],move.getJump()[1],self.pins[move.getJump()[0]][move.getJump()[1]];
        #print move.getEnd()[0],move.getEnd()[1],self.pins[move.getEnd()[0]][move.getEnd()[1]];

        #Empty Start
        #0
        if(self.pins[move.getStart()[0]][move.getStart()[1]]=="0" or self.pins[move.getStart()[0]][move.getStart()[1]]=="-"):
            #print "Validmove() start returns false"
            #print "-------------------------------------------------------";
            return False;

        #Empty Jump Over
        #0
        if(self.pins[move.getJump()[0]][move.getJump()[1]]=="0" or self.pins[move.getStart()[0]][move.getStart()[1]]=="-"):
            #print "Validmove() jump returns false"
            #print "-------------------------------------------------------";
            return False;

        #Filled in End
        #1
        if(self.pins[move.getEnd()[0]][move.getEnd()[1]]=="X" or self.pins[move.getStart()[0]][move.getStart()[1]]=="-"):
            #print "Validmove() end returns false"
            #print "-------------------------------------------------------";
            return False;
        #print "Validmove() returns true"
        #print "-------------------------------------------------------";
        return True;

    def jump(self,move):
        #print "In jump() of GamBoard Class";
        #print "==============================Board Before Valid Jump=============================="
        #get previous configuration
        gb=self.copy_previous_gameboard();#copy values from previous object

        #Early Detection Before Jump
        if(gb.finalBoard()):
            sys.exit("Found The Solution...Before Jump")

        print "==============================Jump Details Start=============================="

        print "Start Position::",(move.getStart()[0]),(move.getStart()[1]);
        print "Jump Position::",(move.getJump()[0]),(move.getJump()[1]);
        print "End Position::",(move.getEnd()[0]),(move.getEnd()[1]);

        for row_val in gb.pins:
            print row_val

        #jump
        gb.pins[move.getStart()[0]][move.getStart()[1]]="0";#0
        gb.pins[move.getJump()[0]][move.getJump()[1]]="0";#0
        gb.pins[move.getEnd()[0]][move.getEnd()[1]]="X";#
        print "              "

        #Display GameBoard After Valid Jump

        for row_val in gb.pins:
            print row_val

        print "Location Details::"
        print "<"+str(gb.locations[move.getStart()[0]][move.getStart()[1]])+","+str(gb.locations[move.getEnd()[0]][move.getEnd()[1]])+">";

        print "==============================Jump Details End=============================="


        #Early Detection After Jump
        if(gb.finalBoard()):
            print ""
            print "Time Required To Execute The Program::",(time.time() - self.start_time)
            print ""
            sys.exit("Found The Solution...After Jump")
            print ""


        #exit("board");
        return gb;


    def copy_previous_gameboard(self):
        #print "copy_previous_gameboard(self) of GameBoard Class"

        #Assigns First Gameboard Configuration
        gb=GameBoard();

        #print "================================================="
        for i in range(0,7):
            for j in range(0,7):
                gb.pins[i][j]=self.pins[i][j]

        #Early Detection Copy Previous Gamboard()
        if(gb.finalBoard()):
            sys.exit("Found The Solution...While Copying Gameboard")

        return gb;

    def finalBoard(self):
        #print "In finalBoard() of GameBoard Class"
        remainingPins=0

        for i in range(0,7):
            for j in range(0,7):
                if(self.pins[i][j]!="-"):
                    if(self.pins[i][j]=="X"):

                        remainingPins=remainingPins+1;

                        #optimize, early out, more than 1 pin is not final board
                        if(remainingPins>1):
                            #print "Required Board Configuration Not Found::";
                            return False;

        #one more check that only [3][3] should have X value
        if(remainingPins==1 and self.pins[3][3]=="X"):
            #print self.pins;
            print "-----------Required Board Configuration Found-----------";
            return True;





