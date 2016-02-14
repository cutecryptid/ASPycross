size_x(n).
size_y(m).

row(1..n).
col(1..m).
symbol(o;x).

sym_cell(x,X,0) :- row(X).
sym_cell(x,X,m+1) :- row(X).
sym_cell(x,0,Y) :- col(Y).
sym_cell(x,n+1,Y) :-  col(Y).

1 {sym_cell(S,X,Y) : symbol(S)} 1 :- row(X), col(Y).

row_adj_black(X,Y,Y1) :- sym_cell(o,X,Y), sym_cell(o,X,Y1), Y1 == Y+1.
col_adj_black(Y,X,X1) :- sym_cell(o,X,Y), sym_cell(o,X1,Y), X1 == X+1.
row_adj_black(X,Y,Y) :- sym_cell(o,X,Y).
col_adj_black(Y,X,X) :- sym_cell(o,X,Y).

h_path(X,Y,L) :- sym_cell(o,X,Y), sym_cell(o,X,Y1), Y1 >= Y, L:= Y1-Y+1,
				row_adj_black(X,Y..Y1-1,Y+1..Y1).
h_path(X,Y,1) :- sym_cell(o,X,Y).
h_block(X,Y,L) :- h_path(X,Y,L), sym_cell(x,X,SY), sym_cell(x,X,PY), SY = Y-1, PY = Y+L.

empty_row(X) :- m{sym_cell(x,X,1..m)}m, row(X).
empty_col(Y) :- n{sym_cell(x,1..n,Y)}n, col(Y).

v_path(X,Y,L) :- sym_cell(o,X,Y), sym_cell(o,X1,Y), X1 >= X, L:= X1-X+1,
				col_adj_black(Y,X..X1-1,X+1..X1).
v_path(X,Y,1) :- sym_cell(o,X,Y).
v_block(X,Y,L) :- v_path(X,Y,L), sym_cell(x,SX,Y), sym_cell(x,PX,Y), SX = X-1, PX=X+L.

:- h_hint(X,0,0), not empty_row(X).
:- v_hint(Y,0,0), not empty_col(Y).

right_h_hint(X,N,L) :- h_hint(X,N,L), L > 0, h_block(X,Y,L).
right_v_hint(Y,N,L) :- v_hint(Y,N,L), L > 0, v_block(X,Y,L).

out_cell(S,X,Y) :- sym_cell(S,X,Y), X > 0, X <= n, Y > 0, Y <= m.

#maximize[right_h_hint(_,_,_) @ 2].
#maximize[right_v_hint(_,_,_) @ 1].

#hide.
#show out_cell/3.
#show size_x/1.
#show size_y/1.