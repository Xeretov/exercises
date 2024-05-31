# Gioele Amendola
# 30/05/2025

# There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

# You are given a 2D array queries, which contains two types of queries:

#       For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin.
#       It is guaranteed that there is no obstacle at distance x when the query is asked.

#       For a query of type 2, queries[i] = [2, x, sz].
#       Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line,
#       such that the block entirely lies in the range [0, x].
#       A block cannot be placed if it intersects with any obstacle, but it may touch it.
#       Note that you do not actually place the block. Queries are separate.

# Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

def block_queries(queries: list[list[int]]) -> list[bool]:
    blocks: list[int] = [0]
    result: list[bool] = []
    for query in queries:
        if len(query) == 2:
            not_append: bool = False
            index: int = 0
            for i,x in enumerate(blocks):
                if query[1] < x:
                    not_append = True
                    index = i
                    break
            if not_append:
                blocks.insert(index,query[1])
            else:
                blocks.append(query[1])
        else:
            before: list = [x for x in blocks if x<=query[1]]
            i, prev = before[-1], before[-2]
            max_size = i-prev
            if max_size >= query[2]:
                result.append(True)
            else:
                result.append(False)
    return result

if __name__ == "__main__":
    print(block_queries([[1,2],[2,3,3],[2,3,1],[2,2,2]]))
    print(block_queries([[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]))
