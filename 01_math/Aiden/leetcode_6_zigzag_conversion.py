class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array = [[] for i in range(numRows)]
        increase = True
        index = 0
        stringBuffer = ""
        
        if numRows == 1:
            return s
        
        for char in s:
            if index == 0:
                increase = True
            elif index == numRows-1:
                increase = False
            
            array[index].append(char)
            
            index = index+1 if increase else index-1
            
        for str in array:
            stringBuffer += "".join(str)
        
        return stringBuffer