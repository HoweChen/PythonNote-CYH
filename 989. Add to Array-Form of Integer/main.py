class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # method 1
        # 语法糖方法
        # return list(map(int,list(str(int("".join(map(str,A)))+K))))

        # method 2
        # 从后往前加k，超过10加一个carry
        for i in range(len(A))[::-1]:
            A[i], K = (A[i] + K) % 10, (A[i] + K) // 10
        return [int(i) for i in str(K)] + A if K else A
