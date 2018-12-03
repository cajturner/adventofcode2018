
class FabricSpec:
    def __init__(self, spec_string: str):
        spec_string = spec_string.rstrip('\n')
        self.id, rest = spec_string.split(' @ ')
        cordinate, size = rest.split(': ')
        self.x, self.y = [int(item) for item in cordinate.split(',')]
        self.width, self.height = [int(item) for item in size.split('x')]

    def __repr__(self):
        return str(self.__dict__)


def calculate_duplicate_fabric(fabric_spec):
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]
    duplicate_square_inch = set()

    for fabric_spec in fabric_specs:
        for width_index in range(fabric_spec.width):
            x = fabric_spec.x + width_index
            for height_index in range(fabric_spec.height):
                y = fabric_spec.y + height_index
                if fabric[x][y] == 1:
                    duplicate_square_inch.add((x,y))
                fabric[x][y] +=1
    return len(duplicate_square_inch)   


def find_non_overlap(fabric_spec):
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]
    duplicate_square_inch = set()

    for fabric_spec in fabric_specs:
        for width_index in range(fabric_spec.width):
            x = fabric_spec.x + width_index
            for height_index in range(fabric_spec.height):
                y = fabric_spec.y + height_index
                if fabric[x][y] == 1:
                    duplicate_square_inch.add((x,y))
                fabric[x][y] +=1
    
    for fabric_spec in fabric_specs:
        overlap_found = False
        for (dup_x, dup_y) in duplicate_square_inch:
            if overlap_found:
                break
            if dup_x >= fabric_spec.x and dup_x <= fabric_spec.x + fabric_spec.width:
                if dup_y >= fabric_spec.y and dup_y <= fabric_spec.y + fabric_spec.height:
                    overlap_found = True
                    break
        if overlap_found is False:
            return fabric_spec.id

with open('day3input.txt') as f:
    fabric_specs = [FabricSpec(item) for item in f.readlines()]
#star1
print(calculate_duplicate_fabric(fabric_specs))
#star2
print(find_non_overlap(fabric_specs))
