from logic import newton_raphson


def main() -> int:
    c = [1, 3, 1]

    dt = newton_raphson(c, 40)
    r = dt["x_n+1"].iloc[-1]
    print(dt)
    print(f"\nraíz ≈ {r}\n" +
          f"     ≈ {float(r)}")

    return 0


if __name__ == "__main__":
    exit(main())
