class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = set([0])
        room_num = 0
        room_q = [0]
        visited = [0]
        while room_q:
            room_num = room_q.pop(0)
            if room_num in keys:
                for key in rooms[room_num]:
                    if key == room_num:
                        continue
                    keys.add(key)
                    if key not in visited:
                        room_q.append(key)
                        visited.append(key)
            
        
        
        return len(keys) == len(rooms)