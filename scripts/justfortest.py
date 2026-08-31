line = line.strip()

        if not line:
            continue

        line = line.split(',')
        sepal_length = float(line[0])
        total += sepal_length

print(f'Sepal length total: {total}')