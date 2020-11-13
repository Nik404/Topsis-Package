# Topsis-Package
# What is TOPSIS
TOPSIS is an acronym that stands for ‘Technique of Order Preference Similarity to the Ideal Solution’ and is a pretty straightforward MCDA method. As the name implies, the method is based on finding an ideal and an anti-ideal solution and comparing the distance of each one of the alternatives to those. It was presented in Hwang and Yoon (Multiple attribute decision making: methods and applications. Springer, Berlin, 1981) and Chen and Hwang (Fuzzy multiple attribute decision making methods. Springer, Berlin, 1992), and can be considered as one of the classical MCDA methods that has received a lot of attention from scholars and researchers. It has been successfully applied in various instances.

# How to ise this Package:
TOPSIS-Nikhal-101816034 can be run by typing the following code snippet:

# In Command Prompt
python topsis.py "data.csv" "1,1,1,2" "+,+,-,+" "Result.csv"

# Sample Dataset
The decison-matrix should be constructed with each row representing a model alternative and each column representing criterian such as accuracy,$\{R}^2$
