% Base case: factorial of 0 is 1.
factorial(0, 1).

% Recursive case: factorial of N is N * factorial of (N-1).
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,           % N-1
    factorial(N1, Result1), % factorial of N-1
    Result is N * Result1.  % multiply N with the result of factorial(N-1)
