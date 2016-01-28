size_x(n).
size_y(m).

row(1..n).
col(1..m).
symbol(o;x).
cell(1..n, 1..m).

1 {sym_cell(S,X,Y) : symbol(S)} 1 :- row(X), col(Y).

out_cell(S,X,Y) :- sym_cell(S,X,Y), X > 0, X <= n, Y > 0, Y <= m.

#hide.
#show out_cell/3.
#show size_x/1.
#show size_y/1.