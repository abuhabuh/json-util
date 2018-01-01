"""Evaluate json object for certain values
"""


def get_val(json_dict, access_list):
    """
    :param json_dict: dict, dict object to get value from
    :param access_list: str or list, access list str with keys and indices
        e.g. 'animal, cat, 1' will get 'garfield' from
            {'animal: {'cat': ['john', 'garfield', 'felix']}}
    """
    if isinstance(access_list, list):
        return _get_val_from_list(json_dict, access_list)
    if isinstance(access_list, str) or isinstance(access_list, unicode):
        actual_list = _to_list(access_list)
        return _get_val_from_list(json_dict, actual_list)
    return None


def _get_val_from_list(json_dict, access_list):
    if not isinstance(json_dict, dict) or not isinstance(access_list, list):
        return None

    if len(access_list) == 0:
        return None

    inner_dict = json_dict
    for field in access_list:
        if isinstance(field, str) or isinstance(field, unicode):
            if not isinstance(inner_dict, dict):
                return None
            inner_dict = inner_dict.get(field, None)
        elif isinstance(field, long) or isinstance(field, int):
            if not isinstance(inner_dict, list) \
                    or field >= len(inner_dict) \
                    or field < -len(inner_dict):
                return None
            inner_dict = inner_dict[field]

        if inner_dict is None:
            return None

    value = inner_dict
    if isinstance(value, str) or \
            isinstance(value, unicode) or \
            isinstance(value, int) or \
            isinstance(value, long):
        return value

    return None


def _to_list(list_str):
    list_str = list_str.strip()
    if len(list_str) == 0:
        return []

    elements = [el.strip() for el in list_str.split(',')]
    idx = 0
    for el in elements:
        try:
            number_el = int(el)
            elements[idx] = number_el
        except ValueError:
            # if we get ValueError parsing el, then assume it's a string
            # if it's a string, it could be a number string wrapped in double
            # quotes to escape treatment as index, so check for that
            if len(el) > 2 and el[0] == '"' and el[-1] == '"':
                try:
                    num_str = int(el[1:-1])
                    elements[idx] = el[1:-1]
                except ValueError:
                    pass
            pass

        idx += 1

    return elements
