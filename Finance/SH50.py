import akshare as ak
import pandas as pd
import numpy as np
import scipy.optimize as sco
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tqdm import tqdm


SH50_codes = [600010, 600028, 600030, 600031, 600036,
              600048, 600050, 600089, 600104, 600111,
              600196, 600276, 600309, 600406, 600436,
              600438, 600519, 600690, 600745, 600809,
              600887, 600893, 600900, 600905, 601012,
              601066, 601088, 601166, 601225, 601288,
              601318, 601390, 601398, 601628, 601633,
              601668, 601669, 601728, 601857, 601888,
              601899, 601919, 603259, 603260, 603288,
              603501, 603799, 603986, 688111, 688599]
SH50_codes = list(map(str, SH50_codes))

df = {}
today = datetime.now().strftime("%Y%m%d")
three_years_ago = (datetime.now() - relativedelta(years=3)).strftime("%Y%m%d")


# 计算每日对数收益率
for i in tqdm(SH50_codes, desc='Downloading'):
    df[i] = ak.stock_zh_a_hist(symbol=i, start_date=three_years_ago, end_date=today)
    df[i]['lnR'] = np.log(df[i]['收盘'] / df[i]['收盘'].shift(1))

# 计算sh50的每日对数收益率
SH50_index = ak.index_zh_a_hist(symbol='000016', start_date=three_years_ago, end_date=today)
SH50_index['lnR'] = np.log(SH50_index['收盘'] / SH50_index['收盘'].shift(1))

rm_list = list(SH50_index['lnR'][1:])

beta_list = []

# 计算sh50的方差
SH50_var = np.var(SH50_index['lnR'][1:])

# 计算每支股票的beta系数
# beta = cov(r, rm)/var(rm)
# rm, returns of the marker
for code in tqdm(SH50_codes, desc='Processing'):
    beta = np.cov(df[code]['lnR'][1:], SH50_index['lnR'][1:])[0, 1] / SH50_var
    beta_list.append(beta)

risk_free_return = np.log(1 + 0.03) / 252

def cal_expect_return(rf, bt, rm):
    """
    expect_return = risk_free_return + beta * (market_expect_return - risk_free_return)
    """
    return rf + bt * (rm - rf)


for code, beta in tqdm(zip(SH50_codes, beta_list), desc='Processing'):
    Er = [np.nan]
    for market_expect_return in rm_list:
        Er.append(cal_expect_return(risk_free_return, beta, market_expect_return))
    df[code]['R'] = pd.DataFrame(Er)

data_log_1 = []

for code in tqdm(SH50_codes, desc='Processing'):
    data_log_1.append([code, ak.stock_individual_info_em(symbol=code).at[5, 'value'], df[code]['R'].mean(),
                       (df[code]['R'].mean() - risk_free_return) / np.std(df[code]['R'])])

data_log_1 = pd.DataFrame(data_log_1, columns=['code', 'name', 'r_mean', 'sharpe_ratio'])
data_log_2 = data_log_1[data_log_1['sharpe_ratio'] > 0].sort_values(by='sharpe_ratio', ascending=False)
data_log_2 = data_log_2[: (data_log_2.shape[0] if data_log_2.shape[0] <= 8 else 8)]

corr_matrix = []
for code_i in list(data_log_2['code']):
    temp = []
    for code_j in list(data_log_2['code']):
        temp.append(df[code_i]['lnR'][1:].corr(df[code_j]['lnR'][1:]))
    corr_matrix.append(temp)
corr_matrix = np.array(corr_matrix)

# https://zhuanlan.zhihu.com/p/268157564

r = np.array([list(data_log_2['r_mean'])]).T
sigma = np.matrix(corr_matrix)
ones = np.ones([r.size, 1])

a = np.dot(np.dot(r.T, sigma.I), r)
b = np.dot(np.dot(ones.T, sigma.I), r)
c = np.dot(np.dot(ones.T, sigma.I), ones)
d = a * c - b * b

w = np.dot(sigma.I, ones) / c

weights = w.T.tolist()[0]
names = list(data_log_2['name'])

for name, weight in zip(names, weights):
    print("# ", name, round(weight * 100, 2), "%")

print('\n预期收益率：', round((np.exp(np.dot(w.T, r) * 252) - 1)[0, 0] * 100, 2), "%")

# https://zhuanlan.zhihu.com/p/60499205?utm_id=0
def stats(w):
    weights = np.array([w])
    port_returns = np.dot(weights, r)
    port_std = np.sqrt(np.dot(np.dot(weights, sigma.I), weights.T))
    return np.array([port_returns, port_std, port_returns / port_std])


def min_sharpe(w):
    return -stats(w)[2]


def min_var(w):
    return stats(w)[1]


len = len(data_log_2)
x0 = len * [1. / len]

bnds = tuple((0, 1) for x in range(len))

cons = ({
    'type': 'eq',
    'fun': lambda x: np.sum(x) - 1
})

opts = sco.minimize(
    min_sharpe,
    x0,
    method='SLSQP',
    bounds=bnds,
    constraints=cons
)

optv = sco.minimize(
    min_var,
    x0,
    method='SLSQP',
    bounds=bnds,
    constraints=cons
)

weights2 = optv['x'].tolist()

for name, weight in zip(names, weights2):
    print('# ', name, round(weight * 100, 2), "%")

print('\n预期收益率：', round((np.exp(stats(optv['x'])[0, 0, 0] * 252) - 1) * 100, 2), "%")
