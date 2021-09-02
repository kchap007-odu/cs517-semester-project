import re


def parse_text_file(filename):
    """Parses core data from text file.

    Args:
        filename (string): The name of the file containing the core data.

    Returns:
        list: a list of lists containing core data.
    """
    cores = [[], [], [], []]

    # Hack-y way to check the encoding of the file.
    try:
        with open(filename) as f:
            f.readline()
        enc = "utf-8"
    except UnicodeDecodeError:
        enc = "utf-16"
    except FileNotFoundError:
        print(f"no file named {filename} found.")
        return []

    with open(filename, 'r', encoding=enc) as f:
        for line in f:
            array = [cores[i].append(float(data))
                     for i, data in enumerate(re.findall(r'[\d]+[.]?[\d+]', line))]
    return cores
