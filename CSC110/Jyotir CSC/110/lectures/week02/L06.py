
def propositional_formula(p: bool, q: bool, r: bool) -> bool:
    """Return the value of ((p ⇒ q) ∧ r) ⇔ (p ⇒ (q ∧ r)).

    >>> propositional_formula(True, False, False)
    True
    >>> propositional_formula(False, False, False)
    False
    """
    s1 = (not p or q) and r
    s2 = (not p) or (q and r)
    return s1 == s2
