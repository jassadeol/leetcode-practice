class Solution:
  #greedy algorithm
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        numOfIntervals = len(intervals)
        intervals.sort(key = lambda x: x[0])
        tempHolder = intervals[0]
        listOfIntervals  = []
        
        for i in range(1, numOfIntervals):
            if (tempHolder[0] <= intervals[i][0] <= tempHolder [1]):
                tempHolder = [tempHolder[0], max(tempHolder[1], intervals[i][1])]
            else:
                listOfIntervals.append(tempHolder)
                tempHolder = intervals[i]
                
        listOfIntervals.append(tempHolder)
        
        return listOfIntervals

        

        
