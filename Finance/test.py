import akshare as ak
import pandas as pd
import numpy as np
from tqdm import tqdm
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scipy.optimize import minimize


def fetch_risk_free_rate():
    return 0.03


def fetch_sh50_code():
    return list(map(str, [600010, 600028, 600030, 600031, 600036,
                          600048, 600050, 600089, 600104, 600111,
                          600196, 600276, 600309, 600406, 600436,
                          600438, 600519, 600690, 600745, 600809,
                          600887, 600893, 600900, 600905, 601012,
                          601066, 601088, 601166, 601225, 601288,
                          601318, 601390, 601398, 601628, 601633,
                          601668, 601669, 601728, 601857, 601888,
                          601899, 601919, 603259, 603260, 603288,
                          603501, 603799, 603986, 688111, 688599]))


def fetch_stock_name(code_list):
    res = []
    for code in tqdm(code_list, desc='获取股票名字：'):
        res.append(ak.stock_individual_info_em(symbol=code).at[1, 'value'])
    return res


def fetch_stock_price_data(code_list):
    res = pd.DataFrame({'日期': []})
    for code in tqdm(code_list, desc='获取收盘价：'):
        data = ak.stock_zh_a_hist(symbol=code, start_date=three_years_ago, end_date=today)[['日期', '收盘']]
        data.rename(columns={'收盘': code})
        res = pd.merge(res, data, on='日期', how='outer')
    return res


today = datetime.now().strftime("%Y%m%d")
three_years_ago = (datetime.now() - relativedelta(years=3)).strftime("%Y%m%d")
risk_free_rate = fetch_risk_free_rate()
sh50_code = fetch_sh50_code()
# sh50_name = fetch_stock_name(sh50_code)
sh50_price_data = fetch_stock_price_data(sh50_code)

"""
sh50_daily_log_return = calc_stock_daily_return(sh50_price_data)
sh50_expected_return = calc_stock_expected_return(sh50_daily_log_return)
sh50_std = calc_stock_std(sh50_daily_log_return)
sh50_sharpe_ratio = calc_stock_sharpe_ratio(sh50_expected_return, risk_free_rate)
sh50_cov_matrix = calc_cov_matrix(sh50_daily_log_return)
"""

print(sh50_price_data.tail())
