import numpy as np 
def hungarian(C):
    n = C.shape[0]
    C -= C.min(axis=0, keepdims = True)
    C -= C.min(axis=1, keepdims = True)
    marked = np.zeros((n,n),dtype=int)
    col_covered = np.zeros(n,dtype=bool)
    row_covered = np.zeros(n,dtype=bool)

    for r in range(n):
        for c in range(n):
            if C[r,c] == 0 and not row_covered[r] and not col_covered[c]:
                marked[r,c] = 1 
                row_covered[r] = True 
                col_covered[c] = True 
    row_covered.fill(False)
    col_covered.fill(False)
    step = 3 
    while step != 7:
        if step == 3:
            col_covered.fill(False)
            for r in range(n):
                for c in range(n):
                    if marked[r,c] == 1:
                        col_covered[c] = True 
            if col_covered.sum() >= n:
                step = 7 
            else:
                step = 4 
        elif step == 4:
            zero_found = False 
            while not zero_found:
                r_idx,c_idx = -1,-1 
                for r in range(n):
                    if not row_covered[r]:
                        for c in range(n):
                            if not col_covered[c] and C[r,c] == 0:
                                r_idx,c_idx = r,c 
                                break 
                        if r_idx != -1:
                            break 
                if r_idx == -1:
                    zero_found = True 
                    step = 5
                else:
                    marked[r_idx,c_idx] = 2
                    star_col = -1 
                    for c in range(n):
                        if marked[r_idx,c] == 1:
                            star_col = c
                            break 
                    if star_col != -1:
                        row_covered[r_idx] = True 
                        col_covered[c_idx] = False 
                    else:
                        path_start = (r_idx,c_idx)
                        zero_found = True 
                        step = 6 
        elif step == 5:
            mask = np.outer(~row_covered,~col_covered)
            min_val = C[mask].min()
            C[~row_covered,:] -= min_val 
            C[:,col_covered] += min_val 
            step = 4 
        elif step == 6:
            path = [path_start]
            while True:
                last_r,last_c = path[-1]
                star_r = -1 
                for r in range(n):
                    if marked[r,last_c] == 1:
                        star_r = r 
                        break 
                if star_r == -1:
                    break 
                path.append((star_r,last_c))
                last_r,last_c = path[-1]
                prime_c = -1 
                for c in range(n):
                    if marked[last_r,c] == 2:
                        prime_c = c 
                        path.append((last_r,prime_c))
                        break
            for r,c in path:
                if marked[r,c] == 1:
                    marked[r,c] = 0 
                else:
                    marked[r,c] = 1 
            marked[marked==2] = 0
            row_covered.fill(False)
            col_covered.fill(False)
            step = 3
    
    return marked 

