# Частотный анализ — это подсчёт, какие символы чаще встречаются в тексте.
# Это важнейший инструмент взлома многих классических шифров —
# от шифра Цезаря до шифровальной машины «Энигма».
# Выполним простой частотный анализ: выясним, какой символ чаще всего
# встречается в данном тексте.

# Входные данные:
# Произвольный текст

import collections

counter = collections.Counter(
    '''
Частотный анализ — это подсчёт, какие символы чаще встречаются в тексте.
Это важнейший инструмент взлома многих классических шифров —
от шифра Цезаря до шифровальной машины «Энигма».
Выполним простой частотный анализ: выясним, какой символ чаще всего
встречается в данном тексте.
    '''
)
print("counter3.most_common()-->", counter.most_common(2))
