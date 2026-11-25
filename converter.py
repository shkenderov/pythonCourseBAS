def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    for c in [0, 20, 37, 100]:
        print(f"{c} °C = {celsius_to_fahrenheit(c)} °F")
    for f in [32, 68, 212]:
        print(f"{f} °F = {fahrenheit_to_celsius(f)} °C")