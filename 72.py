def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32
    X = target_f - current_f
    if X == 0:
        return f"Hold"
    elif X > 0:
        return f"Heat: {X:.1f} degrees Fahrenheit"
    elif X < 0:
        X *= -1
        return f"Cool: {X:.1f} degrees Fahrenheit"


print(adjust_thermostat(72, 18))