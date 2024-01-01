def accumulative_sum_2d(g):
    nrow = len(g)
    ncol = len(g[0])
    A = [[(0) for _ in range(ncol)] for _ in range(nrow)]
    for r in range(nrow):
        for c in range(ncol):
            A[r][c] = (g[r][c] 
                        + (A[r][c-1] if c>0 else 0) 
                        + (A[r-1][c] if r>0 else 0))
    
    return A





        