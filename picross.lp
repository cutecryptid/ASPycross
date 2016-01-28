row(1..n).
col(1..m).
symbol(o;x).
cell(1..n, 1..m).

{sym_cell(S,X,Y) : symbol(S)} :- row(X), col(Y).

#hide.
#show sym_cell/3.