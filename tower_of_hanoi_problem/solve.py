#!/usr/bin/env/python3

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)
def print_rods(rods):
    for rod, disks in rods.items():
        print(f"{rod}: {disks}")
def tower_of_hanoi_visual(n, source, auxiliary, target):
    rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print("Initial state:")
    print_rods(rods)
    print("\nMoving disks:")
    move_disks(n, source, auxiliary, target, rods)
    print("\nFinal state:")
    print_rods(rods)
def move_disks(n, source, auxiliary, target, rods):
    if n == 1:
        move_disk(source, target, rods)
        return
    move_disks(n-1, source, target, auxiliary, rods)
    move_disk(source, target, rods)
    move_disks(n-1, auxiliary, source, target, rods)
def move_disk(source, target, rods):
    disk = rods[source].pop()
    rods[target].append(disk)
    print(f"Move disk {disk} from {source} to {target}")
    print_rods(rods)

num_disks = 4
tower_of_hanoi_visual(num_disks, 'A', 'B', 'C')

# num_disks = 10
# tower_of_hanoi_visual(num_disks, 'A', 'B', 'C')
