import numpy as np
import matplotlib.pyplot as plt

#folder = "D:/SGLC/assignment 2/Q1/"
folder = "C:/Users/Namratha Kaipa/Downloads/assignment_2/assignment_2/Q1/"

# customize path to include our library spam_lib
import sys
sys.path.append(folder)

# import our spam_lib
from lib.spam_lib import classify_messages

# Example usage
file_path = folder+'SMSSpamCollection.txt'
acc_list = []
threshold_list = np.arange(1, 10)
for threshold in threshold_list:
    acc = classify_messages(file_path, threshold=threshold)
    acc_list.append(acc)

plt.bar(threshold_list, acc_list, color='g')
plt.plot(threshold_list, acc_list, color='red', lw=2)
plt.ylim(80, 100)
plt.xlabel("threshold")
plt.ylabel("accuracy(%)")
plt.title("Spam prediction on SMS data")
plt.show()
