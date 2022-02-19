from functools import cache
inp = open('sample.txt','r').read()

"""
schema(?) for each scanner
scanners
    - scanner
        - orientation reversing function
        - beacons
            beacon
                - all beacons relative to it
"""

negative_functions = [
    lambda a: [-a[0], a[1], a[2]],
    lambda a: [a[0], -a[1], a[2]],
    lambda a: [a[0], a[1], -a[2]],
    lambda a: [-a[0], -a[1], a[2]],
    lambda a: [a[0], -a[1], -a[2]],
    lambda a: [-a[0], a[1], -a[2]],
    lambda a: [-a[0], -a[1], -a[2]],
    lambda a: [a[0], a[1], a[2]],
]

rotation_functions = [
    (
        lambda a: [a[0], a[1], a[2]],
        lambda a: [a[0], a[1], a[2]],
    ),
    (
        lambda a: [a[2], a[0], a[1]],
        lambda a: [a[1], a[2], a[0]],
    ),
    (
        lambda a: [a[1], a[2], a[0]],
        lambda a: [a[2], a[0], a[1]],
    )
]

@functools.cache
def orientations():
    """
    gets the 24 orientation functions (must be cached)

    Returns:
    a list having 2 element lists in the format [orientation function: reversing function]
    """
    for negative_func in negative_functions:
        for rotation_func, reverse_rotation_func in rotation_functions:
            yield [
                lambda point: negative_func(rotation_func(point)),
                lambda point: reverse_rotation_func(negative_func(point))
            ]

for i in range(5):
    for tr, rev in orientations():
        print(tr([1,2,3]), rev(tr([1,2,3])))