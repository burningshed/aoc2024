
import numpy as np

def AoCHelpers():
    pass
class coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tup = (x,y)
        
    def __eq__(self, other):
        if isinstance(other, coord):
            if self.x == other.x and self.y == other.y:
                return True
            return False
        else:
            print(f"warning! comparing coord to non-coord \nNon-coord is of type {other}")
            return False
    
    def __hash__(self) -> int:
        return hash(self.tup)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return coord(x,y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return coord(x,y)
                    
    def __str__(self) -> str:
        return f"{self.x, self.y}"
    def __repr__(self) -> str:
        return self.__str__()
    
    def __gt__(self, other):
        if not isinstance(other, coord):
            raise Exception
        if self.x > other.x and self.y > other.y:
            return True
        return False
        
    def __ge__(self, other):
        if not isinstance(other, coord):
            raise Exception
        if self.x > other.x or self.y > other.y:
            return True
        return False
    def __lt__(self, other):
        if not isinstance(other, coord):
            raise Exception
        if self.x < other.x and self.y < other.y:
            return True
        return False
        
    def __le__(self, other):
        if not isinstance(other, coord):
            raise Exception
        if self.x < other.x or self.y < other.y:
            return True
        return False
                    
def data_to_arr(data):
    return [[x for x in y] for y in data.splitlines()]

class flat_map_np:
    def __init__(self, data):
        self.flat_map = np.array(data_to_arr(data))
        self.boundries = self.flat_map.shape
    def check_boundries(self, point_arr):
        """Checks in points in point_arr are within flat_maps boundries.

        Args:
            point_arr (numpy array (of points)): Array of points (in form returned by argwhere)

        Returns:
            bool array: array mirroring point_arr with which elements of point arr are within the boundires of flat_map
        """
        x_valid = np.logical_and(point_arr[:,0] >= 0, point_arr[:,0] < self.flat_map.shape[0])
        y_valid = np.logical_and(point_arr[:,1] >= 0, point_arr[:,1] < self.flat_map.shape[1])
        return np.logical_and(x_valid, y_valid)
        
        