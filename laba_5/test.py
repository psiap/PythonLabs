def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


if '__main__' == __name__:
    print(12)
    file_name = 'test.csv'
    csv_gen = (row for row in open(file_name))
    print(csv_gen.__next__())