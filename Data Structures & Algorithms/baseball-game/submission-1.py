class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for ops in operations:
            if ops == '+':
                add = res[-2] + res[-1]
                res.append(add)
            elif ops == 'D':
                mul = 2 * res[-1]
                res.append(mul)
            elif ops == 'C':
                res.pop()
            else:
                res.append(int(ops))
        return sum(res)