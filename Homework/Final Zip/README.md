1 (a) [5 points] If kickoff is at noon, at what time should you start preparing your bratwurst so that
you don’t miss any of the game?

Running, eclps -b bratwurst.ecl -e ’schedule(EndTime)’ it takes 40 min for a solution to be found.

So to not miss the kickoff at 12:00 AM, you should prepare your bratwurst at 11:20 AM.


2.

1) 

mkrolic1@ugradx:~/Declarative Methods/Homework 2$ eclps -b ninetriangles.ecl -e "generateAllAssignments"
MySolution = [17, 19, 20, 21, 23].

2) 

mkrolic1@ugradx:~/Declarative Methods/Homework 2$ eclps -b concat.ecl -e "generateAllAssignments"
MySolution = [[142, 857]].

3)

mkrolic1@ugradx:~/Declarative Methods/Homework 2/Problem2$ eclps -b isotriangle.ecl -e "generateAllAssignments"
MySolution = [[48, 40, 40], [72, 45, 45], [120, 65, 65]].

4) 

mkrolic1@ugradx:~/Declarative Methods/Homework 2$  eclps -b funfive.ecl -e "generateAllAssignments"
MySolution = 200.

5)


mkrolic1@ugradx:~/Declarative Methods/Homework 2$  eclps -b smallestsquare.ecl -e "generateAllAssignments"
Found a solution with cost 35172
Found no solution with cost 33334.0 .. 35171.0
MySolution = 35172.



4.b)


For part 4, I retrofitted the existing bratwurst.ecl file to the new problem format.

I first set up a few scripts to generate:
- the tasks
- the duration clauses
- the precedence ordering
- the start and finish arrays

I then piped those results into a few files, which then I would copy and paste back into the bratwurst file, modifying it for each component. Additionally I removed the resource constraints and removed the sorting order so that the output would be ordered by the task name. After which I ran the file, piped the output into a solution file.

6.

a) 

The lowest total time schedule that satisfies all of the constraints I found was 36950.


The constraints I used one occupancy, task time durations and precedence ordering.

In calling search, I used the parameters: 
- AllVars
- 0
- smallest
- indomain_split
- complete
- []

The best total time I found was 36950.


To find the cost it took me roughly 15 minutes.
It took me 11.89 seconds to find the assignment after having knowing the cost.  

b)

To start out, I ran the algorithm 30 times with a 3 min timeout with different parameters to find the best solution route. I then ran the best candidates for 20 minutes each to find optimal solutions.

My explanation for why the algorithm works well with the search paramters smallest and indomain_split is that this problem is a schedule optimization problem, which can be solved efficiently using a greedy algorithm. The smallest parameters makes it so that the algorithm explores the variables with the smallest start time first and then schedules later events, surfacing conflicts and corresponding resolutions early.

Indomain_split uses binary search to split the domain in two halves. As noted on the eclipseclp wiki, this can sometimes suface errors earlier and additionally binary search is O(log n), which tends to be faster than linear search especically in larger intervals. 

c)

If I was not constrained by the choices in search, I would probably pick tasks based on how many tasks they have scheduled after them. This would be to prevent situations where a lot of smaller tasks are completed first and then there is a slow pipeline that has to be done one at a time at the end, with no parallelization. 

For value ordering, I would stick with indomain_min or indomain_split. 

d)

The code for the above is attached and the parsers are in a folder called parsers Which was used to generate the clauses for the Eclipse program.