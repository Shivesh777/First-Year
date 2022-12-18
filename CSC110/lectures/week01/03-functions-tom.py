def fahrenheit_to_celsius(deg_f: float) -> float:
    """Return the celsius temperature corresponding to
    to the fahrenhit measure deg_f.

    >>> fahrenheit_to_celsius(80.0)
    26.666666666666668
    >>> fahrenheit_to_celsius(0.0)
    -17.77777777777778

    """

    return (deg_f - 32) * 5 / 9
