from collections import Counter

class Box:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

def solve(file_path):
    boxes = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            box_c = line.split(",")
            boxes.append(Box(box_c[0], box_c[1], box_c[2]))
    
    n = len(boxes)
    
    edges = []
    for i in range(n):
        box1 = boxes[i]
        for j in range(i + 1, n):
            box2 = boxes[j]
            dx = box1.x - box2.x
            dy = box1.y - box2.y
            dz = box1.z - box2.z
            dist_sq = dx*dx + dy*dy + dz*dz
            edges.append((dist_sq, i, j))
    
    edges.sort()
    
    parent = list(range(n))
    size = [1] * n
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True
    
    for i in range(min(1000, len(edges))):
        dist_sq, a, b = edges[i]
        union(a, b)
    
    component_sizes = Counter()
    for node in range(n):
        root = find(node)
        component_sizes[root] += 1
    
    sizes = sorted(component_sizes.values(), reverse=True)
    print(sizes)
    result = sizes[0] * sizes[1] * sizes[2]
    return result

if __name__ == "__main__":
    file_path = r""
    answer = solve(file_path)
    print(f"Result: {answer}")
