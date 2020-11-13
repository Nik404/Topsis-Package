import numpy as np
import pandas as pd
import sys
from scipy.stats import rankdata

def main():
	if len(sys.argv)!=5:
		print("Wrong paramenters")
		exit(1)

	df = pd.read_csv(sys.argv[1]).values
	x = df[:,1:]
	weight = [int(i) for i in sys.argv[2].split(',')]
	impact = sys.argv[3].split(',')
	topsis(x,weight,impact)

def topsis(matrix,weight,impact):
	dimension = matrix.shape
	if len(weight) !=  dimension[1]:
		return print("Error! lenght of weight is not equal to number of column")
	if len(impact) != dimension[1]:
		return print("Error! len of impact is not equal to number of column")

	if not all(i>0 for i in weight):
		return print("Weight must be positive")
	if not all(i=="+" or i == "-" for i in impact):
		return print("Impact must be a char vector of '+' and '-' sign")

	data = np.zeros([dimension[0]+2,dimension[1]+4])
	total = sum(weight)
	for i in range(dimension[1]):
		for j in range(dimension[0]):
			data[j,i] = (matrix[j,i]/np.sqrt(sum(matrix[:,i]**2)))*weight[i]/total

	for i in range(dimension[1]):
		data[dimension[0],i] = max(data[:dimension[0],i])
		data[dimension[0]+1,i] = min(data[:dimension[0],i])

		if impact[i] == "-":
			data[dimension[0],i] ,data[dimension[0]+1,i] = data[dimension[0]+1,i] , data[dimension[0],i]


	for i in range(dimension[0]):
		data[i,dimension[1]] = np.sqrt(sum(data[dimension[0],:dimension[1]] - data[i,:dimension[1]]**2))
		data[i,dimension[1]+1] = np.sqrt(sum(data[dimension[0]+1,:dimension[1]] - data[i,:dimension[1]]**2))
		data[i,dimension[1]+2] = data[i,dimension[1]+1]/(data[i,dimension[1]] + data[i,dimension[1]+1])


	data[:dimension[0],dimension[1]+3] = len(data[:dimension[0],dimension[1]+2]) - rankdata(data[:dimension[0],dimension[1]+2]).astype(int) + 1
	ans = {"Model": np.arange(1,dimension[0]+1), "Score": data[:5,dimension[1]+2], "Rank": data[:5,dimension[1]+3]}


	my_df=pd.DataFrame(ans)
	my_df.to_csv(sys.argv[4], index=False)

if __name__ == "__main__":
	main()

