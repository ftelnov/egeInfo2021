filename = input()

with open(filename) as file:
    data = list(map(lambda x: tuple(map(int, x.split())), file.readlines()[1:]))
    forged_data = []
    m_sum = 0
    for item in data:
        m_sum += min(item)
        forged_data.append(max(item) - min(item))
    if m_sum % 8 == 2:
        m_sum += min(forged_data)
    print(m_sum)
