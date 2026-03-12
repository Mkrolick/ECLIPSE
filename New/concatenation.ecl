:- lib(ic).			% include the standard interval constraint library
:- lib(branch_and_bound).	% include the branch and bound library for minimization
:- lib(ic_edge_finder).		% include the cumulative constraint library needed for resource constraints
:- lib(lists).		% for printing ordered solution


generateAssignments(X, Y) :-
	SubAssignments = [X, Y],
    SubAssignments :: 100..999,

    6 * (X * 1000 + Y) #= (Y * 1000 + X),

    labeling(SubAssignments).

solve(MySolution) :-
    findall([X, Y], generateAssignments(X, Y), AllXAndYs),
    sort(AllXAndYs, MySolution).
