def valid_interval(interval):
    if interval[0] > interval[1]:
        print("Invalid interval: a must be less than b")
        return False
    return True
    
def bolzano_condition(f, interval):
    if f(interval[0])*f(interval[1]) >= 0:
        print("Bolzano condition not satisfied: f(a) and f(b) must have different signs")
        return False
    return True

def belongs(x, I):
    valid_interval(I)
    if x > I[1] or x < I[0]:
        print("Value does not belong to the interval.")
        return