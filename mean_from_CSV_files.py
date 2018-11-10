import pandas as pd


def CSV_mean(path, column, trial, stop):
    file = "/".join([path, 'analize/consolidated' + ".csv"])
    data = pd.read_csv(file)
    mean_file = "/".join([path, 'analize/mean_file' + ".csv"])
    # print(data)
    df = pd.DataFrame(columns=('generation', column))
    max = data['generation'].max()
    sizes = data.groupby(['generation']).size()
    means = data.groupby('generation', as_index=False)[column].mean()
    print(max)
    for line in range(0, max):
        # print(sizes[line])
        # print(means['mean_fit'][line])
        print(line)
        mean = means['mean_fit'][line] * ((sizes[line + 1]) / trial) + \
            stop * ((trial - sizes[line + 1]) / trial)
        df = df.append(pd.DataFrame([[line + 1, mean]], columns=('generation', column)))
        # print(df)
    # print(df)
    # data = data.append(df)
    # df.append(df2)
    # means = data.groupby('generation', as_index=False)[column].mean()
    # print(means)

    df.to_csv(mean_file, sep=',')
    return('Done')
