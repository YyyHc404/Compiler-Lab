def StringToInterger(str:str) -> int:
    t = 0
    for c in str:
        t = t*10 + int(c,10)
    return t 