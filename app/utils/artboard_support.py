def supports_artboards(file_data):
    """
    Determines if a given file supports artboards based on its details.
    """
    # Placeholder logic - replace with actual criteria for determining artboard support
    return "artboards" in file_data and len(file_data["artboards"]["Boards"]) > 0

def get_artboards(file_data):
    """
    Returns the artboards supported by a given file.
    """
    # Placeholder logic - replace with actual criteria for determining artboard support
    return file_data["artboards"]["Boards"]