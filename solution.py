import itertools
print(
    *itertools.accumulate(
        list(
            map(
                int, 
                input().split()
            )
        ),
        lambda x, y: x + y
    )
)
