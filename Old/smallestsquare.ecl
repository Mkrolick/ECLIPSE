:- lib(ic).			% include the standard interval constraint library
:- lib(branch_and_bound).	% include the branch and bound library for minimization
:- lib(ic_edge_finder).		% include the cumulative constraint library needed for resource constraints
:- lib(lists).		% for printing ordered solution


generateAssignments(N, X1, X2, X3, X4, X5, X6, X7, X8, X9, X10) :-
	StartAssignments = [X1],
    StartAssignments :: 1..9,

    MiddleAssignments = [X2, X3, X4, X5, X6, X7, X8, X9, X10],
    MiddleAssignments :: 0..9,

    N :: 33334..100000,

    RX1 #= X1 * 1000000000,
    RX2 #= X2 * 100000000,
    RX3 #= X3 * 10000000,
    RX4 #= X4 * 1000000,
    RX5 #= X5 * 100000,
    RX6 #= X6 * 10000,
    RX7 #= X7 * 1000,
    RX8 #= X8 * 100,
    RX9 #= X9 * 10,
    RX10 #= X10,

    LHS #= RX1 + RX2 + RX3 + RX4 + RX5 + RX6 + RX7 + RX8 + RX9 + RX10,
    LHS #= N * N,

    append(StartAssignments, MiddleAssignments, AllNums),
    alldifferent(AllNums),


    append(AllNums, [N], Solution),
    minimize(labeling(Solution), N).

generateAllAssignments :-
    generateAssignments(N, _, _, _, _, _, _, _, _, _, _),
    printf("MySolution = %w.%n", [N]).
