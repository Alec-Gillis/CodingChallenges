  
"""
Got an initial solution working pretty quickly, but the runtime was a big yikes. Knew I wanted to keep track of capacity as trips started/ended, 
and that I'd only return false if capacity < 0. My approach is always to get a solution down and working, then optimize. I worked on optimizations
for 23 minutes to no avail in my IDE, at which point I would typically start googling for help, but I was fed up so I went straight for a solution
in the discussion posts. Turns out a priority queue is a nice way to keep track of which trip ends next. No problem, did a refresher on pq's (especially the python library to import).
In a typical whiteboarding interview I don't think I'd have a problem importing a DS that I need without having the correct syntax as long as I get my point across,
but with everything over the internet with COVID, I have a feeling I'm going to need to know the DS imports & methods off of the top of my head...

Stats:
Time: ~7 minutes for passing solution, 23 minutes of attempted optimizations before reading discussion posts
Runtime: 1128 ms, faster than 5.10% of Python3 online submissions for Car Pooling.
Memory Usage: 14.3 MB, less than 55.16% of Python3 online submissions for Car Pooling.
Speed: O(m * n)  [ m = len(trips) ]
Storage: O(1)
"""


from operator import itemgetter

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        open_seats = capacity
        counter = 0
        while counter != len(trips):
            # looped through every trip 
            for i, trip in enumerate(trips):
                #check if trip starts at current distance
                if trip[1] == 0:
                    open_seats -= trip[0]
                trips[i][1] -= 1
                #check if trip ends at current distance
                if trip[2] == 0:
                    open_seats += trip[0]
                    #increment counter for trips completed
                    counter += 1
                trips[i][2] -= 1
            if open_seats < 0:
                return False       
        return True
