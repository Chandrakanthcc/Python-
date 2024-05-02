try:
    a=10
    b=4
    c=a*b
    print(c)
except Exception as e:
    print(f"error ocuured:{e}")
finally:
    print("done")
    