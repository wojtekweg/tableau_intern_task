def select(data_in, start_time, delta):
    temp = select_given_key(data_in, 'resolution', "Confirmed")
    temp = select_within_time_range(temp, start_time, delta)
    return temp


def select_given_key(data_in, key, status):
    """
    Function returns only the rows with the given :status: key.
    """
    temp = []
    for d in data_in:
        if d[key] == f"{status}":
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
