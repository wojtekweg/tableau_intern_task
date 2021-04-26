# TODO wrap data cleaning into a class, so the data_in parameter won't be needed to pass and returned as the side-effect
#  in each method
import re
from dateutil import parser


def clean(data_in, severity_scale=(1, 2, 3, 4)):
    """
    :param: Expected format should contain following keys
    "issue_code":
    "created_at":
    "severity":
    "resolution":
    "affected_components":
    "creator_id":
    :return: Cleaned data, ready for its processing.
    """
    add_key(data_in, "notes")
    clean_affected_components(data_in)
    clean_created_at(data_in)
    clean_creator_id(data_in)
    clean_issue_code(data_in)
    clean_resolution(data_in)
    clean_severity(data_in, severity_scale)


# Cleaning of each keys


def clean_affected_components(data_in):
    """
    - expected input: {'{Content}', ... '{Guides}', '{Sign-up}'}
    - Delete parenthesis in all components.
    - Delete all "-", "_" and " ".
    """
    for d in data_in:
        d['affected_components'] = \
            remove_parenthesis_symbols(
                remove_not_alphanumeric(d['affected_components'])).capitalize()


def clean_created_at(data_in):
    """
    - expected input: {'', '13/04/2021 17:03:58', '13/04/2021 18:58:48', ...}
    - Change all dates into Python's datetime object.
    - Estimate the date by checking date above and below and note that fact.
    """
    # convert dates to proper date format
    for d in data_in:
        if d["created_at"] != "":
            d["created_at"] = parser.parse(d["created_at"])

    # for the objects with no date provided, estimate it
    it = -1
    for d in data_in:
        it += 1
        if d["created_at"] == "":
            d["created_at"] = parser.parse(calculate_average_date(data_in, it))
            d["notes"] += "Date is estimated."


def clean_creator_id(data_in):
    """
    - expected input: {'', '1765', '8058', '4693', '1120', '4075' ...}
    - If there is no creator ID, write default creator_id = 0000
    """
    for d in data_in:
        if d["creator_id"] == "":
            d["creator_id"] = "0000"
            d["notes"] += "Creator ID was not provided."


def clean_issue_code(data_in):
    """
    - expected input: {'CYCLE-10-75', 'CYCLE-10-68', 'CYCLE-10-39', ..., 'CYCLE-10-11', '10-88', 'CYCLE-1096'}
    - Delete "CYCLE-" prefix.
    - Split Cycle ID to major and minor, by the "-" sign.
    - If ID has no "-", check it's previous and next ID.
    """
    # add new keys
    add_key(data_in, "id_maj")
    add_key(data_in, "id_min")

    # delete prefix in issue_code, store the maj and min number
    it = -1
    for d in data_in:
        it += 1
        # delete prefix, if present
        if d["issue_code"][0:3] == "CYC":
            d["issue_code"] = d["issue_code"][6:]

        # split ID and store it split
        d["id_maj"] = d["issue_code"].rpartition('-')[0]
        d["id_min"] = d["issue_code"].rpartition('-')[2]

        # if one of IDs was not extracted
        if d["id_maj"] == "" or d["id_min"] == "":
            # take the previous major id and try to extract the minor from given cycle id
            try:
                prev_id_maj = data_in[previous_nonempty_param(data_in, it, "id_maj")]["id_maj"]
                d["id_maj"] = prev_id_maj
                d["id_min"] = d["issue_code"].rpartition(prev_id_maj)[2]
                d["notes"] += "Issue code was edited."
            except IndexError:
                print("[ ERROR ] issue_code wasn't successfully extracted. Please, review your data.")


def clean_resolution(data_in):
    """
    - expected input: {'No tester response', 'Confirmed (!)', 'Expected Behaviour', 'Invalid - not tester error',
'Not in Scope', 'Confirmed (S)', 'Duplicate', 'Confirm (S)'}
    - Delete all letters in parenthesis, (S) or (!) should be deleted
    - Add "-ed" suffix to 'confirm'.
    # TODO make string matching more generic (it is impossible to do with given amount of data)
    """
    it = -1
    add_key(data_in, "resolution_status")
    for d in data_in:
        it += 1
        d["resolution"] = extract_resolution_status(d, d["resolution"])\
            .capitalize()

        # single cases
        if "Confirm" in d["resolution"]:
            d["resolution"] = "Confirmed"
        if "tester" in d["resolution"]:
            d["notes"] += f"Original resolution was '{d['resolution']}'"
            d["resolution"] = "Not tester error"
    pass


def clean_severity(data_in, scale):
    add_key(data_in, "severity_weight")
    severity_mapping = {
        "Low": scale[0],
        "Medium": scale[1],
        "High": scale[2],
        "Critical": scale[3]
    }
    for d in data_in:
        d["severity_weight"] = severity_mapping[d["severity"]]


# Utilities helpful for cleaning process


def add_key(data_in, key):
    for d in data_in:
        d[key] = ""


def remove_parenthesis_symbols(word):
    return re.sub(r'[{()}]', '', word)


def extract_resolution_status(d, word):
    """
    Extract the resolution status which is wrapped in '(x)' and store it as another column.
    """
    subtracted = re.sub(r'\([^)]*\)', '', word)
    if len(subtracted) < len(word):
        d["resolution_status"] = word[len(subtracted):]
        subtracted = subtracted[:-1]  # delete the space at the end
    return subtracted


def remove_not_alphanumeric(word):
    return re.sub('[^a-zA-Z]+', '', word)


def calculate_average_date(data_in, it):
    """
    :param data_in: Dictionary with data containing dates.
    :param it: Iterator is needed, so it will be possible to iterate for next and previous element.
    """
    if it == 0:
        avg_date = data_in[next_nonempty_param(data_in, it, 'created_at')]['created_at']
    elif it == len(data_in):
        avg_date = data_in[previous_nonempty_param(data_in, it, 'created_at')]['created_at']
    else:
        next_date = data_in[next_nonempty_param(data_in, it, 'created_at')]['created_at']
        prev_date = data_in[previous_nonempty_param(data_in, it, 'created_at')]['created_at']
        avg_date = prev_date + (next_date - prev_date) / 2
    return str(avg_date)


def previous_nonempty_param(data_in, index, param):
    i = 0
    while data_in[index - i][param] == "":
        i += 1
        if index - i < 0:
            raise Exception(f"Impossible to estimate the date, check your {param}")
    return index - i


def next_nonempty_param(data_in, index, param):
    i = 0
    while data_in[index + i][param] == "":
        i += 1
        if index + i > len(data_in):
            raise Exception(f"Impossible to estimate the date, check your {param}")
    return index + i
