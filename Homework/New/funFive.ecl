:- lib(ic).			% include the standard interval constraint library
:- lib(branch_and_bound).	% include the branch and bound library for minimization
:- lib(ic_edge_finder).		% include the cumulative constraint library needed for resource constraints
:- lib(lists).		% for printing ordered solution


generateAssignments(X1, X2, X3, X4, X5) :-
	StartAssignments = [X1],
    StartAssignments :: 1..9,

    MiddleAssignments = [X2, X3, X4],
    MiddleAssignments :: 0..9,

    EndAssignments = [X5],
    EndAssignments :: [8,6,4,2,0],

    X5 #= X1 + X2 + X3 + X4,

    labeling(StartAssignments),
    labeling(MiddleAssignments),
    labeling(EndAssignments).


solve(MySolution) :-
    findall([X1, X2, X3, X4, X5], generateAssignments(X1, X2, X3, X4, X5), AllSolutions),
    length(AllSolutions, MySolution).
