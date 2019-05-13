from z3 import *
i0, j0 = Ints('i0 j0')
i1, j1 = Ints('i1 j1')
i2, j2 = Ints('i2 j2')
i3, j3 = Ints('i3 j3')
i4, j4 = Ints('i4 j4')
i5, j5 = Ints('i5 j5')
i6, j6 = Ints('i6 j6')
i7, j7 = Ints('i7 j7')
i8, j8 = Ints('i8 j8')
i9, j9 = Ints('i9 j9')
i10, j10 = Ints('i10 j10')

F = And(i0 == 0 , j0 == 1 , 
	    i1==i0+1, j1==j0+2,
	    i2==i1+1, j2==j1+2, 
	    i3==i2+1, j3==j2+2,
	    i4==i3+1, j4==j3+2,
	    i5==i4+1, j5==j4+2,
	    i6==i5+1, j6==j5+2,
	    i7==i6+1, j7==j6+2, 
	    i8==i7+1, j8==j7+2,
	    i9==i8+1, j9==j8+2,
	    i10==i9+1, j10==j9+2,
	    )

prove(Implies(F, j10 < 18))