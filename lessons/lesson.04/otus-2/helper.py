def get_least(*args):
    args = [el for el in args if el >= 0]
    return min(args)
