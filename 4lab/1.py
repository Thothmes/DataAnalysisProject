import numpy as np
import pandas as pd


#1
start_numbers_seria = pd.Series(np.random.normal(loc=1, scale=1, size=1000))
print(start_numbers_seria)

#2
start_loc = start_numbers_seria.mean()
mask_1 = (start_numbers_seria >= start_loc-1) & (start_numbers_seria <= start_loc+1)
standard_deviaton_interval_s1 = start_numbers_seria[mask_1]

#3
"""  По сути  "правило трёх сигм". 
Когда нам требуются числа в диапазоне [M-3s;M+3s] 
теоретическая вероятность попадания в интервал составляет 99.73% 
Решение -> P(-3 < X < 3) = Ф(3) - Ф(-3), где Ф(X) - функция X ~ N(0,1)"""

mask_2 = (start_numbers_seria >= start_loc-3) & (start_numbers_seria <= start_loc+3)
standard_deviaton_interval_s3 = start_numbers_seria[mask_2]
print(f"Теоретическая вероятность попадания составляет: 99,73%. Фактическая у серии: {(standard_deviaton_interval_s3.size/start_numbers_seria.size)*100}%")

#4
root_seria = pd.Series(np.sqrt(start_numbers_seria))
print(root_seria)

"""Предупреждение возникает из-за невозможности найти квадратный корень из отрицательного числа, 
т.к если он есть, то sqrt(x)^2 в любом случае будет положительным, что не соблюдается при наличии отр.числа"""

#5
#root_seria_without_NaN = pd.Series.dropna(root_seria) - возможно, но след.вариант лучше
print(root_seria.mean(skipna=False))

#6
dataframe = pd.DataFrame({"number":start_numbers_seria, "root":root_seria})
print(dataframe.iloc[0:6])

#7
print(dataframe.query('root >= 1.8 & 1.9 >= root'))