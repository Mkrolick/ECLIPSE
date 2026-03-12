:- lib(ic).			% include the standard interval constraint library
:- lib(branch_and_bound).	% include the branch and bound library for minimization
:- lib(ic_edge_finder).		% include the cumulative constraint library needed for resource constraints
:- lib(lists).		% for printing ordered solution


generateAssignments(PossibleN) :-
	TriangleAssignments = [PA, PB, PC, PD, PE, PF, PG, PH, PI],
	TriangleAssignments :: 1..9,

	alldifferent(TriangleAssignments),

    V1 #= PA + PB + PC + PD,
    V2 #= PB + PE + PF + PG,
    V3 #= PD + PH + PI + PG,

    V1 #= V2,
    V2 #= V3,
    V1 #= PossibleN,

    labeling(TriangleAssignments).

generateAllAssignments :-
    findall(PossibleN, generateAssignments(PossibleN), AllNs),
    sort(AllNs, SortedAssignments),
    printf("MySolution = %w.%n", [SortedAssignments]).
