def supports_artboards(file_data):
    """
    Determines if a given file supports artboards based on its details.
    """
    return "artboards" in file_data and file_data["artboards"]["Supported"] and file_data["artboards"].get("Boards")


def get_artboards(file_data):
    """
    Returns the artboards supported by a given file.
    """
    if "artboards" in file_data and file_data["artboards"]["Supported"]:
        return file_data["artboards"].get("Boards", [])
    return []