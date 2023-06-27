def filter_on_attributes(attribute_set: set, request) -> dict:
    """
        filter helper._
        builds a dictionary with the query parameters if provided
    """
    return {k: request.GET.get(k) for k in attribute_set if request.GET.get(k) is not None}
