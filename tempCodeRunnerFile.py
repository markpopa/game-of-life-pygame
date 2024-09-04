        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
