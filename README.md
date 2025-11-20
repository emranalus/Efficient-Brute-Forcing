# Efficient-Brute-Forcing
A way of slashing the brute forced bit string in half which is %50 logarithmically efficient! 

# How It Works?
Normally brute forcing a bit string is O(2^n) hard because every slot can get 2 values the floor is 2 where n is the length of the bit string
but because every bit string is a repeatation of other bitstrings and lower n strings are exponentially easier to calculate we can use those to calculate our new bitstring for example:

bb - 2 bits

00 = A,
10 = B,
01 = C,
11 = D

I calculated the every possible combination of the 2 bit string and then I labeled them as A, B, C, D
now I will use labels to calculate a new bit string!

AA
AB
AC
AD
BA
BB
BC
BD
CA
CB
CC
CD
DA
DB
DC
DD

If I see AA I will decode that as 0000 = AA (because A = 00) this calculation when done normally is equal to O(2^4) but with this method its big O notation is O(2^2 + 4^2) so the big O notation of my algorithm is O(2^(n/2)) which is more efficient!
