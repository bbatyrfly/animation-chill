a = int(input())
b = int(input())
c = int(input())
d = int(input())

a_1 = a
b_1 = b
c_1 = c
d_1 = d
a_2 = a
b_2 = b
c_2 = c
d_2 = d

if a_1 < b_1:
    b_1 = a_1
if b_1 < c_1:
    c_1 = b_1
if c_1 < d_1:
    d_1 = c_1

if a_2 > b_2:
    b_2 = a_2
if b_2 > c_2:
    c_2 = b_2
if c_2 > d_2:
    d_2 = c_2

if d_1 < a < d_2:
    d_3 = a
if d_1 < b < d_2:
    d_3 = b
if d_1 < c < d_2:
    d_3 = c
if d_1 < d < d_2:
    d_3 = d

if d_1 < a < d_3 or d_3 < a < d_2:
    d_4 = a
if d_1 < b < d_3 or d_3 < b < d_2:
    d_4 = b
if d_1 < c < d_3 or d_3 < c < d_2:
    d_4 = c
if d_1 < d < d_3 or d_3 < d < d_2:
    d_4 = d

if d_3 < d_4:
    print(d_1, d_3, d_4, d_2)
else:
    print(d_1, d_4, d_3, d_2)
    
