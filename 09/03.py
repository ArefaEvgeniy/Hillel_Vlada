input_data = [
    34,
    67,
    12,
    -678,
    [
        679,
        10,
        0,
        (
            888,
            99,
            -987,
            [
                67,
                89,
                90,
                (
                    100,
                    200,
                    -300,
                    [
                        400,
                        500,
                        600
                    ]
                )
            ]
        ),
    ],
    5,
    9
]


def main(number, data):
    result = False
    for item in data:
        if isinstance(item, int) and item == number:
            result = True
            break
        elif isinstance(item, (list, tuple)):
            result = main(number, item)
            if result:
                break

    return result


print(main(600, input_data))
