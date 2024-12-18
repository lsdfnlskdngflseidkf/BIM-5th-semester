% Base case: Moving 1 disk from Source to Destination.
hanoi(1, Source, Destination, _) :-
    write('Move disk from '), write(Source),
    write(' to '), write(Destination), nl.

% Recursive case: Moving N disks.
hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Destination),  % Move N-1 disks to Auxiliary peg.
    hanoi(1, Source, Destination, _),         % Move the largest disk to Destination peg.
    hanoi(M, Auxiliary, Destination, Source). % Move N-1 disks to Destination peg.
