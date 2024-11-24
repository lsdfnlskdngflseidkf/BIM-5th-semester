male(rijan).
male(harry).
male(ishan).
male(krish).

female(shreya).
female(mira).
female(jenny).
female(riya).

parent(rijan,harry).
parent(rijan,mira).
parent(shreya,mira).
parent(shreya,harry).

parent(jenny,krish).
parent(harry,krish).
parent(mira,riya).
parent(ishan,riya).

mother(X,Y):-parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).

grandfather(X,Z):-father(X,Y),parent(Y,Z).

grandmother(X,Z):-mother(X,Y),parent(Y,Z).

sister(X,Y):-parent(Z,X),parent(Z,Y),female(Y),X\==Y.

brother(X,Y):-parent(Z,X),parent(Z,Y),male(Y),X\==Y.

