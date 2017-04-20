class BinarySearch(list):
    
    def __init__(self, length, step):
        """class constructor method"""
        super(BinarySearch, self).__init__()
        # populate the class based on the length and step arguments
        for elem in range(1, length+1):
            self.append(elem * step)
        # define a length attribute
        self.length = len(self)

    def search(self, val):
        # initialize the first and last indices
        first = 0
        last = len(self) - 1
        value_index = 0
        found = False
        # initialize counter
        counter = 0
        # check if val is the first or last element
        if val == self[first]:
            value_index = first
            found = True
        elif val == self[last]:
            value_index = last
            found = True
        # check if val is not present in the list
        if val not in self:
            found = True
            value_index = -1
        # binary search algorithm using a while loop
        while first <= last and not found:
            mid = (first + last) // 2
            if self[mid] == val:
                found = True
                value_index = mid
            else:
                counter += 1  # update counter when an interaction occurs
                if val < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return {'count': counter, 'index': value_index}
