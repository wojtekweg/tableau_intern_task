from datetime import timedelta


def select(data_in, start_time):
    temp = select_resolution(data_in, "Confirmed")
    temp = select_within_time_range(temp, start_time, timedelta(hours=6))
    return temp


def select_resolution(data_in, status):
    """
    Function returns only the rows with the given :status: key.
    """
    temp = []
    for d in data_in:
        if d["resolution"] == f"{status}":
            temp.append(d)
    return temp


def select_within_time_range(data_in, start_time, time_delta):
    """
    Function returns only the rows that are less than :start_time: + :time_delta:
    """
    temp = []
    counted_delta = start_time + time_delta
    for d in data_in:
        if d["created_at"] <= counted_delta:
            temp.append(d)
    return temp
