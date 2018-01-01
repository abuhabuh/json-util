import json


def parse(json_dict, access_list):
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
