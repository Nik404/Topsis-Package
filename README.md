# Topsis-Package
# What is TOPSIS
TOPSIS is an acronym that stands for ‘Technique of Order Preference Similarity to the Ideal Solution’ and is a pretty straightforward MCDA method. As the name implies, the method is based on finding an ideal and an anti-ideal solution and comparing the distance of each one of the alternatives to those. It was presented in Hwang and Yoon (Multiple attribute decision making: methods and applications. Springer, Berlin, 1981) and Chen and Hwang (Fuzzy multiple attribute decision making methods. Springer, Berlin, 1992), and can be considered as one of the classical MCDA methods that has received a lot of attention from scholars and researchers. It has been successfully applied in various instances.

# How to use this Package:
TOPSIS-Nikhal-101816034 can be run by typing the following code snippet:

# In Command Prompt
python topsis.py "data.csv" "1,1,1,2" "+,+,-,+" "Result.csv"

# Sample Dataset
The decison-matrix should be constructed with each row representing a model alternative and each column representing criterian such as accuracy,R-Sqaure,Root Mean Squared error,Correlation etc.

| Model | Corr | Rseq | RMSE | Accuracy |
|-------|------|------|------|----------|
| M1    | 0.79 | 0.62 | 1.25 | 60.89    |
| M2    | 0.66 | 0.44 | 2.89 | 63.07    |
| M3    | 0.56 | 0.31 | 1.57 | 62.87    |
| M4    | 0.82 | 0.67 | 2.68 | 70.19    |
| M5    | 0.75 | 0.56 | 1.3  | 80.39    |

# Output
| Model | Score             | Rank |
|-------|-------------------|------|
| 1     | 0.476957713840877 | 2    |
| 2     | 0.476572577796742 | 3    |
| 3     | 0.477495853743771 | 1    |
| 4     | 0.475616911138615 | 5    |
| 5     | 0.475948812224928 | 4    |

_The Ranking are displayed in the result csv file, with 1st rank offering the best decision and last rank offering the worst decision according to the TOPSIS method._

