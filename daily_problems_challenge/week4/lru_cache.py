class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.key_index_map = {}
        self.index_key_map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        
        # check current index of key
        current_index = self.key_index_map[key]
        if current_index == 0:
            return self.data[key]
        
        # shift indices before current_index
        for index in range(current_index-1, -1, -1):
            cur_key = self.index_key_map[index]
            self.index_key_map[index+1] = cur_key
            self.key_index_map[cur_key] = index + 1
            
        # assign new key to recent index
        self.key_index_map[key] = 0
        self.index_key_map[0] = key
        
        return self.data[key]
            

    def put(self, key: int, value: int) -> None:
        if key in self.data and self.key_index_map[key] == 0:
            self.data[key] = value
            return
        
        if key in self.data:
            current_index = self.key_index_map[key]
        else:
            # check current capacity and adjust if needed
            if len(self.data) == self.capacity:
               # remove the oldest key
                oldest_key = self.index_key_map[self.capacity-1]
                del self.data[oldest_key]
                del self.index_key_map[self.capacity-1]
                del self.key_index_map[oldest_key]
            
            current_index = len(self.index_key_map)
            
        # update data map
        self.data[key] = value
        
       # shift indices before current_index
        for index in range(current_index-1, -1, -1):
            cur_key = self.index_key_map[index]
            self.index_key_map[index+1] = cur_key
            self.key_index_map[cur_key] = index + 1
            
        # assign new key to recent index
        self.key_index_map[key] = 0
        self.index_key_map[0] = key

                
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)