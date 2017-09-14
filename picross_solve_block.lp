% Generate
row(0..height+1).
col(0..width+1).
maxheight(height).
maxwidth(width).

{ hblock(X1, X2, Y, Idx): col(X1), col(X2), X1 <= X2,
    X1 > 0, X1 <= width, X2 > 0, X2 <= width, L = X2-X1+1 } = 1 :- hhint(Y, Idx, L).
{ vblock(X, Y1, Y2, Idx): row(Y1), row(Y2), Y1 <= Y2,
    Y1 > 0, Y1 <= width, Y2 > 0, Y2 <= width, L = Y2-Y1+1 } = 1 :- vhint(X, Idx, L).

% Define
overhblocks(Y, Idx1, Idx2) :- hblock(X11, X12, Y, Idx1), hblock(X21, X22, Y, Idx2),
    X21 >= X11-1, X21 <= X12+1, Idx1 != Idx2.
overvblocks(X, Idx1, Idx2) :- vblock(X, Y11, Y12, Idx1), vblock(X, Y21, Y22, Idx2),
    Y21 >= Y11-1, Y21 <= Y12+1, Idx1 != Idx2.

hcell(X, Y) :- hblock(X1, X2, Y, _), col(X), row(Y), X >= X1, X <= X2.
vcell(X, Y) :- vblock(X, Y1, Y2, _), col(X), row(Y), Y >= Y1, Y <= Y2.

wrongcell(X, Y) :- hcell(X, Y), not vcell(X, Y).

% Test
:- overhblocks(_, _, _).
:- overvblocks(_, _, _).

:- hblock(X11, X12, Y, Idx1), hblock(X21, X22, Y, Idx2), Idx2 > Idx1, X21 < X11.
:- vblock(X, Y11, Y12, Idx1), vblock(X, Y21, Y22, Idx2), Idx2 > Idx1, Y21 < Y11.

:- hhint(Y, _, 0), hcell(X, Y), col(X).
:- vhint(X, _, 0), vcell(X, Y), row(Y).

:- wrongcell(_, _).

% Display
#show maxwidth/1.
#show maxheight/1.
#show hcell/2.
