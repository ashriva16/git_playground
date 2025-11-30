from src import add  # because __init__.py re-exports add


def main() -> None:
    a = 2
    b = 3
    result = add(a, b)
    print(f"{a} + {b} = {result}")


if __name__ == "__main__":
    main()
