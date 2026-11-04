import time


def get_data():

    def get_processor(data):
        pass
        return data

    def get_memory(data):
        pass
        return data

    def get_process(data):
        pass
        return data

    data = {}
    data = get_processor(data)
    data = get_memory(data)
    data = get_process(data)

    return data


def process_data(data):
    pass
    return data


def print_data(data):
    print(data)


def main():
    while True:
        data = get_data()
        new_data = process_data(data)
        print_data(new_data)
        time.sleep(3)


main()
