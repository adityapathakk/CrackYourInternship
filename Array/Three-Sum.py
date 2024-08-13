class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        # splitting nums into 3 lists - negative, positive and zeros

        n, p, z = [], [], []

        for num in nums:
            if num > 0: p.append(num)
            elif num < 0: n.append(num)
            else: z.append(num)

        # creating separate set for -ves and +ves for O(1) look-up

        N, P = set(n), set(p)

        # if at least one zero in the list, add all cases where -num exists in N and num exists in P
        # for eg. (-1, 0, 1) = 0

        if z:
            for num in P:
                if -1 * num in N:
                    result.add((-1 * num, 0, num))

        # if there're at least 3 zeros in the z list, include (0, 0, 0) = 0
        
        if len(z) >= 3: result.add((0, 0, 0))

        # for all pairs of -ve numbers (eg. -3, -1), check for their complement (4) in +ve number set

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    result.add(tuple(sorted([n[i], n[j], target])))

        # for all pairs of +ve numbers (eg. 1, 1), check for their complement (-2) in -ve number set

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    result.add(tuple(sorted([p[i], p[j], target])))

        return result