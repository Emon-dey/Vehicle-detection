import os
import pandas as pd
import numpy as np

directory = './data/'
ref_directory = 'D:/Desktop/data_object/label_2/training/label_2/'
list_dir = os.listdir(directory)

threshold = np.arange(.5,1,.05)
tp = np.zeros(len(threshold))
fp = np.zeros(len(threshold))
fn = np.zeros(len(threshold))
for file in list_dir:
	try:
		predy_file = pd.read_csv(directory + file, sep = ' ', header = None)
		testy_file = pd.read_csv(ref_directory + file, sep = ' ', header = None)
		testy_file = np.array(testy_file[(testy_file[0] == 'Cyclist')].loc[:,4:7], dtype = np.float)
		predy_file = np.array(predy_file[(predy_file[0] == 'Cyclist')].loc[:,4:7], dtype = np.float)
		fp += len(predy_file)
		fn += len(testy_file)
		for k in range(len(threshold)):
			for i in range(len(predy_file)):
				boxB = predy_file[i]
				for j in range(len(testy_file)):
					boxA = testy_file[j]
					xA = max(boxA[0], boxB[0])
					yA = max(boxA[1], boxB[1])
					xB = min(boxA[2], boxB[2])
					yB = min(boxA[3], boxB[3])
					interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
					boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
					boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
					iou = interArea / float(boxAArea + boxBArea - interArea)
					if(iou > threshold[k]):
						tp[k] += 1
						fp[k] -= 1
						fn[k] -= 1
						break
	except:
		print('no file')

	print(file, ' tp  fp  fn ',tp, fp, fn)
file = np.c_[threshold, tp, fp, fn, np.divide(tp,(tp+fp))]
print(file)
np.savetxt('result.csv', file, delimiter=",", fmt ='%.3f')