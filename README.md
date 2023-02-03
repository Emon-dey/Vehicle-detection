### KITTI Dataset Link
```
For maintaing extact formating please download the dataset from google drive.
Drive link: https://drive.google.com/drive/folders/1FbRMOo-L3CtF_PLsgq2aguAP2xB6i1pT?usp=sharing
Please login using umbc mail
```
### Prerequisites 
```
tensorflow-gpu
CUDA v10
```
other dependencies: 
```
opencv-python
open3d-python
scikit-learn
tqdm
shapely
```

## Code run
```
We have run the code using .py file. A iPython file is provided as an example
```
### Argument for data visualization code
```
Mandatory arguments:
checkpoint_path     path to checkpoint [in this case we have use checkpoint as ./ckp/model1]
dataset_root_dir    root path provided in google drive

Semi mandatory arguments:
dataset_split_file  draw bounding box on the mentioned image on that file [by default it will select testfile.txt]
output_dir          output save file
optional arguments:
level LEVEL         visualization level, 0 to disable,1 to nonblocking visualization, 2 to block
test                enable test model
no-box-merge        disable box merge.
no-box-score        disable box score.
```

### Argument for training
```
train_config_path  path from which train file will load configuration [in this case we have use checkpoint as ./train_conf/model1_train_config]
config_path        path from which train file will load complete configuration [in this case we have use checkpoint as ./train_conf/model1_full_config]
dataset_root_dir   root path provided in google drive

Semi mandatory arguments:
dataset_split_file  draw bounding box on the mentioned image on that file [by default it will select testfile.txt]
```
