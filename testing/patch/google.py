from testing.patch.data import get_data, get_data1

def call_googl_api():
    data = get_data()
    return data

def call_googl_api2():
    data = get_data()
    data1 = get_data1()
    return data + data1
