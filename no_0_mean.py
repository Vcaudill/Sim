import pandas as pd


def CSV_mean(path, column, trial, stop):
    file = "/".join([path, 'analize/consolidated' + ".csv"])
    data = pd.read_csv(file)
    mean_file = "/".join([path, 'analize/mean_file' + ".csv"])
    # print(data)
    df = pd.DataFrame(columns=('newgen', column))
    max = data['newgen'].max()
    sizes = data.groupby(['newgen']).size()
    means = data.groupby('newgen', as_index=False)[column].mean()
    # print(max)
    for line in range(0, max):
        # print(line, sizes[line])

        # print(means['mean_fit'][line])
        mean = means['mean_fit'][line] * ((sizes[line + 1]) / trial) + \
            stop * ((trial - sizes[line + 1]) / trial)
        df = df.append(pd.DataFrame([[line + 1, mean]], columns=('newgen', column)))
        # print(df)
    # print(df)
    # data = data.append(df)
    # df.append(df2)
    # means = data.groupby('generation', as_index=False)[column].mean()
    # print(means)

    df.to_csv(mean_file, sep=',')
    return('Done')


'''
basic_PATH = '/Users/victoria/Desktop/Sim/'  # Use your path
folder = "no_0_Loc_10"

stop = .99
trials = 100
column = 'mean_fit'
PATHtoFILES = "".join([basic_PATH, folder + "/" + "popsize_1000/_mu_0.001/"])
# PATH = "".join([basic_PATH, folder + "/"])
# file = "/".join([PATHtoFILES, 'analize/consolidated' + ".csv"])
# data = pd.read_csv(file)
CSV_mean(PATHtoFILES, column, trials, stop)
'''
