def ticket_price(age: int) -> float:
    """Return the ticket price for a person who is age years old.

    Seniors 65 and over pay 4.75, kids 12 and under pay 4.25, and
    everyone else pays 7.50.

    Precondition:
      - age > 0

    >>> ticket_price(7)
    4.25
    >>> ticket_price(21)
    7.5
    >>> ticket_price(101)
    4.75
    """
    if age >= 65:
        return 4.75

    elif age > 12:
        return 7.5
    else:
        return 4.25

