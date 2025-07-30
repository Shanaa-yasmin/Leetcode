class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        fullrow = []
        row = [1]

        for i in range(numRows):
            fullrow.append(row)
            newrow = [1]
            for j in range(1, len(row)):
                newrow.append(row[j - 1] + row[j])
            newrow.append(1)
            row = newrow

        return fullrow
