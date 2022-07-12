import numpy as np
from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt


def diagram():
    X = np.array(eval(input('데이터 집합 {(a,b), (c,d), (e,f)}를 [[a,b], [c,d], [e,f]]의 형태로 입력해주세요.')))
    n = int(input('지속구간 다이어그램의 최대 차원을 적어주세요. 단, 0 이상의 정수만 적어주세요. 예) 2'))
    return plot_diagrams(ripser(X, maxdim=n)['dgms'])


