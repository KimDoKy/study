import csv

with open('sample.csv', mode='r', encoding='utf-8') as read_file:
    reader = csv.reader(read_file)
    next(reader)

    with open('result.tsv', mode='w', encoding='utf-8') as write_file:
        writer = csv.writer(write_file, delimiter='\t')
        writer.writerow(['경기도','인구 밀도(명/km2)'])

        for row in reader:
            population_density = float(row[2]) / float(row[3])
            writer.writerow([row[1], int(population_density)])
