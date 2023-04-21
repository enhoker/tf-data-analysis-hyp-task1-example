import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency


chat_id = 689985882 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    list_for_test = [[x_cnt-x_success, x_success],[y_cnt - y_success, y_success]]
    try:
                stat, p, dof, expected = chi2_contingency(list_for_test)
            except:
                p = -1
    a = True #оставляем канал
    if (y_success / y_cnt > x_success / x_cnt):
      a = False #убираем канал
    if(p>0.02):
      a = False #убираем канал
      
    return a
