:- lib(ic).			% include the standard interval constraint library
:- lib(branch_and_bound).	% include the branch and bound library for minimization
:- lib(ic_edge_finder).		% include the cumulative constraint library needed for resource constraints
:- lib(lists).		% for printing ordered solution


generateAssignments(Base, Side) :-

    Lengths = [Base, Side],
    Lengths :: 1..1000,
    Base #< 2 * Side,

	(Base * Base) * (4 * Side * Side - Base * Base) #= 576 * (Base * Base + 4 * Base * Side + 4 * Side * Side),
	labeling(Lengths).

solve(MySolution) :-
    findall([Base, Side, Side], generateAssignments(Base, Side), MySolution).
