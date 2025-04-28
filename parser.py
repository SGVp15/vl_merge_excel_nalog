import re


def parsing(data: list, header=None) -> []:
    act = data[0][0]
    company = data[1][0]
    company = re.findall(r'".*" и (.*) по договору', company)[0]
    company = re.sub(r'\s*\(.*\)', '', company)

    start_n = 0
    stop_n = 0
    for i, row in enumerate(data):
        if '№' in row:
            if header:
                start_n = i
            else:
                start_n = i + 1
            break
    for i, row in enumerate(data):
        if 'ИТОГО:' in row:
            stop_n = i
            break
    data_out = []
    for i in range(start_n, stop_n):
        data_out.append([*data[i], act, company])
    return data_out
