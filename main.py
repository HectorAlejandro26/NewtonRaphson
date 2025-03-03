from logic import newton_raphson
from fractions import Fraction
from typing import Union


def main() -> int:
    c = [1, 3, 1]

    dt = newton_raphson(c, 40)

    def format_frac(x: Fraction | None) -> float | Fraction | None:
        return float(x) \
            if len(str(x.numerator)) > 9 or len(str(x.denominator)) > 9 \
            else x

    r: Fraction = dt["x_n+1"].iloc[-1]

    dt["x_n"] = dt["x_n"].apply(format_frac)
    dt["f(x)"] = dt["f(x)"].apply(format_frac)
    dt["f'(x)"] = dt["f'(x)"].apply(format_frac)
    dt["x_n+1"] = dt["x_n+1"].apply(format_frac)

    r = format_frac(r)

    print(dt, end='\n\n')

    print(f"raíz ≈ {r}")
    if isinstance(r, Fraction):
        print(f"     ≈ {float(r)}")

    return 0


if __name__ == "__main__":
    exit(main())
