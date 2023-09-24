import math

bricks = int(input())
workers = int(input())
cart_capacity = int(input())

trips = bricks / (workers * cart_capacity)

print(math.ceil(trips))
