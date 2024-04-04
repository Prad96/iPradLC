class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        for operation in range(len(operations)):
            operations[operation]=operations[operation].replace('--X', 'X--').replace('++X', 'X++')
        return operations.count('X++')-operations.count('X--')
    