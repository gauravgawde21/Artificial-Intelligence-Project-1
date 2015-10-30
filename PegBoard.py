from Play import Play;

class PegBoard:

    def __init__(self):
        #print "1.In PegBoard Class Constructor"
        play=Play();

        print "2.Calling dfs() in PegBoard Class"
        play.dfs();

        print "------------------------------------------------------------------------"

        print "3.Calling iddfs() in PegBoard Class"
        #play.iddfs();

        print "------------------------------------------------------------------------"

        print "4.Calling astar with first heuristic in PegBoard Class"
        #play.astar(1);

        print "------------------------------------------------------------------------"

        print "5.Calling astar with second heuristic in PegBoard Class"
        #play.astar(2);

#Start Application
pegboard_obj=PegBoard();
