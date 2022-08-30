import numpy as np
import pandas as pd

# pop_dict = {
#     'china' : 141500,
#     'japan' : 12718,
#     'korea' : 5180,
#     'usa' : 32676,
# }
# population = pd.Series(pop_dict)

# gdp_dict = {
#     'china' : 1409250000,
#     'japan' : 516700000,
#     'korea' : 169320000,
#     'usa' : 2041280000,
# }
# gdp = pd.Series(gdp_dict)

# country = pd.DataFrame({
#     'gdp' : gdp,
#     'population' : population
# })

# print(country)

# data = {
#     'country' : ['china', 'japan', 'korea', 'usa'],
#     'gdp' : [1409250000, 516700000, 169320000, 2041280000],
#     'population' : [141500, 12718, 5180, 32676]
# }

# country = pd.DataFrame(data)
# # print(country)

# country = country.set_index('country')



# country.index.name = 'Country'
# country.columns.name = 'Info'

# gdp_per_capita = country['gdp'] / country['population']
# country['gdp per capita'] = gdp_per_capita

# print(country)

df = pd.DataFrame(columns= [ '이름', '나이', '주소'])
df.loc[0] = ['길동', '26', '서울']
df.loc[1] = {'이름' : '철수', '나이' : '25', '주소' : '인천'}
df.loc[1, '이름'] = '영희'
df['전화번호'] = np.nan
df.loc[0, '전화번호'] = '010-1234-1234'

df.drop('전화번호', axis= 1, inplace= True) # axis = 1 : 열 방향 / axis = 0 : 행방향
      # inplace = True : 원본 변경 / inplace = False : 원본 변경 X
print(df)