import re


def marsExploration(s):
    list_signals = re.findall('...', s)
    length_signal = len(list_signals)
    signal_count = 0
    for signal in list_signals:
        for index, letter in enumerate(signal):
            if index == 0 and letter != 'S':
                signal_count += 1
            if index == 1 and letter != 'O':
                signal_count += 1
            if index == 2 and letter != 'S':
                signal_count += 1
    return signal_count
