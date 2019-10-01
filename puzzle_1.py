import collections
import copy


class Solution(object):
    def slidingPuzzle(self, board):
        lenx = len(board)
        leny = len(board[0])

        def board2str(board):
            bstr = ""
            for i in range(lenx):
                for j in range(leny):
                    bstr += str(board[i][j])
            return bstr

        goal = ''
        for i in range(1, lenx * leny):
            goal = goal + str(i)
        goal = goal + '0'

        solution = []
        start = board2str(board)
        bfs = collections.deque()
        bfs.append((start, 0, solution))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while bfs:

            path, step, solution = bfs.popleft()

            if step == 0:
                visited = set()
                visited.add(path)
            elif step == 20:
                break

            if path == goal:
                for h in range(1, step):
                    print(solution[h])
                    print('\n')

            p = path.index('0')  # la position de 0

            x, y = int(p / leny), p % leny

            path = list(path)  # moving
            for dir in dirs:
                tx, ty = x + dir[0], y + dir[1]
                if tx < 0 or tx >= lenx or ty < 0 or ty >= leny:
                    continue

                path[tx * leny + ty], path[x * leny + y] = path[x * leny + y], path[tx * leny + ty]
                pathStr = "".join(path)

                if pathStr not in visited:
                    bfs.append((pathStr, step + 1, solution + [path]))
                    visited.add(pathStr)

                path[tx * leny + ty], path[x * leny + y] = path[x * leny + y], path[tx * leny + ty]

        return -1


print(Solution().slidingPuzzle([[2, 3, 1], [4, 5, 6], [7, 0, 8]]))

# print(Solution().slidingPuzzle([[1,2,3],[4,5,6],[7,0,8]]))
# print(Solution().slidingPuzzle([[3,1,2],[4,0,5]]))
# print(Solution().slidingPuzzle([[1,2,3],[4,0,5]]))

# print(Solution().slidingPuzzle([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,0,15]]))





