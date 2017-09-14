% Declare Picross Size
% (This may be not neccessary in the near future)

#const height = 5.
#const width = 5.

% Horizontal Hints are the hints for the rows
% The format is hhint(ROW, IDX, LENGTH)
% ROW is the row of the hint
% IDX is the index of the hint, the first would be 0, the second would be 1 and so on
% LENGTH is the number of the hint itself, if the hint says 4, length should be 4

hhint(1, 0, 3).
hhint(2, 0, 2).
hhint(2, 1, 1).
hhint(3, 0, 2).
hhint(3, 1, 2).
hhint(4, 0, 2).
hhint(4, 1, 1).
hhint(5, 0, 2).
hhint(5, 1, 1).

% Vertical Hints are the hints for the rows
% The format is vhint(COL, IDX, LENGTH)
% COL is the column of the hint
% IDX is the index of the hint, the first would be 0, the second would be 1 and so on
% LENGTH is the number of the hint itself, if the hint says 4, length should be 4

vhint(1, 0, 2).
vhint(2, 0, 5).
vhint(3, 0, 2).
vhint(3, 1, 1).
vhint(4, 0, 1).
vhint(4, 1, 1).
vhint(5, 0, 4).

% The hints for this example would be for a Picross like this
%          2 1
%      2 5 1 1 4
% ---------------
%   3 |         |
% 2 1 |         |
% 2 2 |         |
% 2 1 |         |
% 2 1 |         |
% ---------------
