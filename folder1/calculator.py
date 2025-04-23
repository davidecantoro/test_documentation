"""
Modulo di esempio per operazioni di base.
"""

def add(a: float, b: float) -> float:
    """
    Somma due numeri.

    :param a: primo addendo
    :param b: secondo addendo
    :returns: somma di a e b
    :raises TypeError: se a o b non sono numeri
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Entrambi i parametri devono essere numeri")
    return a + b

class Divider:
    """
    Classe per operazioni di divisione.
    """

    def __init__(self, divisor: float):
        """
        :param divisor: valore per dividere
        """
        self.divisor = divisor

    def divide(self, dividend: float) -> float:
        """
        Divide dividend per il divisor di questa istanza.

        :param dividend: valore da dividere
        :returns: risultato della divisione
        :raises ZeroDivisionError: se divisor è zero
        """
        if self.divisor == 0:
            raise ZeroDivisionError("Divisione per zero")
        return dividend / self.divisor
