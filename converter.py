def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


if __name__ == "__main__":
    for c in [0, 20, 37, 100]:
        print(f"{c} °C = {celsius_to_fahrenheit(c)} °F")