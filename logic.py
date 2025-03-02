from typing import Sequence, List, Union
from fractions import Fraction
from pandas import DataFrame


def __eval_func(coefs: Sequence[int], x: float) -> float:
    res: Fraction = 0
    x = Fraction(x)

    for c in coefs:
        res = res * x + Fraction(c)
    return res


def derivar(coefs: Sequence[int]) -> List[int]:
    return [c * e for c, e in zip(coefs, range(len(coefs) - 1, 0, -1))]


def newton_raphson(
    coefs: Sequence[int],
    x: Union[float, Fraction],
    tol=1e-10,
    max_iter=500
) -> DataFrame:

    d_coefs = derivar(coefs)
    x: Fraction = Fraction(x)

    d = {
        "x_n": [],
        "f(x)": [],
        "f'(x)": [],
        "x_n+1": []
    }

    for _ in range(max_iter):
        fx = __eval_func(coefs, x)
        dfx = __eval_func(d_coefs, x)

        d["x_n"].append(x)
        d["f(x)"].append(fx)
        d["f'(x)"].append(dfx)

        if abs(fx) < tol:
            d["x_n+1"].append(None if dfx == 0 else x - Fraction(fx, dfx))
            return DataFrame(d)

        if dfx == 0:
            raise ZeroDivisionError(
                "La derivada se anuló, no se puede continuar.")

        x -= Fraction(fx, dfx)
        d["x_n+1"].append(x)

    raise ValueError(
        "El método no convergió en el número máximo de iteraciones.")
