import numpy as np
import random
import copy

#ランクを計算、掃き出し法でランクを求める
def rank(R):	
	FR = copy.deepcopy(R)
	FRhistory = []
	for i in range(a*n):
		for j in range(a*n):
			if(FR[j][i] == 1 and (j in FRhistory) == False):
				M = copy.deepcopy(FR[j])
				FRhistory.append(j)
				for k in range(a*n):
					if((FR[k][i] == 1) and j !=k):
						FR[k] = FR[k]^M
				break
	for i in range(a*n-1):
		for j in range(a*n):
			if(i != j):
				FR[j] = FR[i]^FR[j]
	rankcount = 0
	for i in FR:
		if(any(i)):
			rankcount = rankcount + 1
	return rankcount 

# フルランク行列を生成．numpyというライブラリを使ってランクを計算
def FullRankMatrix(r):
	while(True):
		R = np.random.randint(2, size=(r,r)) #rxrのランダムバイナリ行列を生成
		rankcount = rank(R)
		if(rankcount == r): #ランクを計算
			return R

# 任意の関数の値の計算
def f(x):
	x = [x[i:i+a] for i in range(0,len(x),a)] # x=(a1,a2)を(a1),(a2)に分割
	x1 = int(x[0],2)
	x2 = int(x[1],2)
	y = x1 & x2 #関数の計算
	y = list(map(int,format(y,'08b'))) #ビット長に直してベクトル化
	return y

#行列Vの計算
def FunctionMatrix(v,onelist):
	V  = np.random.randint(2,size=(a*n,a)) #
	rand = random.randint(0,len(onelist)-1) #
	V[onelist[rand]] = v #
	if(len(onelist) > 2): 
		while(True):
			rand2 = random.randint(0,len(onelist)-1)
			if(rand2 != rand):
				break
	else:
		rand2 = random.randint(0,len(onelist)-1)
	VOneVector = np.array([0] * (a))
	for j in range(len(onelist)):
		if( j != rand and j != rand2):
			VOneVector = VOneVector^V[onelist[j]]
	
	V[onelist[rand2]] = VOneVector
	return V

def RandomMatrix(R,onelist):
	rand = random.randint(0,len(onelist)-1)
	ROneVector = np.array([0] * (n*a))
	for j in range(len(onelist)):
		if( j != rand):
			ROneVector = ROneVector^R[onelist[j]]
	R[onelist[rand]] = ROneVector
	return R

#調整された乱数の生成
def AdjustMatrix():
	AdMatrix = []
	for i in range(pow(pow(2,a),n)-1):
		bit = format(i+1,'016b')
		bitarray = list(map(int,bit))
		v = f(bit)
		R = FullRankMatrix(a*n)
		onelist = []
		for j in range(len(bitarray)):
			if(bitarray[j] == 1):
				onelist.append(j)
		V = FunctionMatrix(v,onelist)
		R = RandomMatrix(R,onelist)
		AdMatrix.append(np.c_[R,V])
		
	return AdMatrix

#乱数確認のテスト
def test(AdMatrix):
	x1 = 15
	X1 = format(x1,'08b')
	print('x1',x1)
	x2 = 9
	X2 = format(x2,'08b')
	print('x2',x2)
	M = 0
	for i in AdMatrix:
		R = separateMatrix(i)
		M1 = user(R[0],X1)
		M2 = user(R[1],X2)
		M = M1^M2
		m = []
		for j in range(a*n):
			m.append(M[j])
		if(any(m) == False):
			print('M',M)

#全ユーザの行列をユーザごとに分割
def separateMatrix(R):
	R = [R[i:i+a] for i in range(0,len(R),a)]
	return R

#ユーザの操作。乱数とxと使って計算
def user(R,x):
	M = np.array([0] * (n*a+a))
	bitx = list(map(int,x))
	for i in range(len(R)):
		if(bitx[i] == 1):
			M = M^R[i]
	return M

n = 2 # ユーザ数
a = 8 # ユーザ一人当たりのビット幅


AdMatrix = AdjustMatrix()

test(AdMatrix)