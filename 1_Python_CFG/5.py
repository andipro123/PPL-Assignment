pageNumbers = [2,4,6,12,16,17,20,21]
for page in range(1, 25):
    if page in pageNumbers:
        continue
    else:
        print(page)
