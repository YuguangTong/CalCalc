# calcalc

Simple calculator based on `Sympy` and `Wolfram Alpha`
- takes string input
- interprets input as math with Sympy.simplify
- request Wolfram Alpha for more non-trivial strings

**Example:**
.. code-block:: python

    >>> from calcalc.CalCalc import calculate
    >>> calculate('mass of the moon in kg',  return_float=True)
    7.3459e+22
    >>> calculate('2 * 3 ** 2 * 5 + 10')
    100
