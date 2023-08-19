for i in range(1, 101):
    not_divided_by_seven = i % 7 != 0
    no_seven = "7" not in str (i)
    if not_divided_by_seven and no_seven:
        print(i)
    else:
        print("boom")