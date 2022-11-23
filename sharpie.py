def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if mat[i][j] != mat[j][i]:
                return False
    return True




print(isSymmetric([[1, 0, 5], [0, 2, 4], [5, 4, 1]], 3))
