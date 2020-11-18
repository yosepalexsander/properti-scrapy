from random import seed, choice
from pathlib import Path
from re import sub


seed(2)


def get_random_ua():
    random_ua = ""
    base_path = Path(__file__).resolve().parent
    ua_file = Path(base_path, "user_agent.txt")
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            random_ua = choice(lines)

    except Exception as ex:
        print("Exception in random user agent")
        print(str(ex))
    finally:
        return random_ua


def string2integer(value):
    """
    Args:
      value: string

    Return:
      integer
    """
    value = sub(r"(\d+)([.,]?)(\d*)[\w\xc2\xb2]+", r"\1\2\3", value)
    return int(value)
