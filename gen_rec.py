import os,sys
import warnings
import shutil

warnings.filterwarnings('ignore')
data_root_dir = 'c:/dataset/cifar/split/'


shutil.copyfile(os.path.join(os.environ.get('MXNET_ROOT'),'tools/im2rec.py') , 'im2rec.py')
print os.path.join(os.environ.get('MXNET_ROOT'),'tools/im2rec.py') 
datasets = ['train','test']

for dataset in datasets:
    cmd = 'python im2rec.py {} {} --recursive --list'.format(
    dataset, os.path.join(data_root_dir,dataset))
    print cmd
    os.system(cmd)
    cmd = 'python im2rec.py {} {} --num-thread 2'.format(
    dataset, os.path.join(data_root_dir, dataset))
    print cmd
    os.system(cmd)
