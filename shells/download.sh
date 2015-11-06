#! /bin/bash

if [ ! -d data ]; then
    mkdir data
fi
cd data

wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/annotations.zip
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set00.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set01.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set02.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set03.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set04.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set05.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set06.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set07.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set08.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set09.tar
wget http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/set10.tar

unzip annotations.zip
rm -rf annotations.zip

tar xvf set00.tar
rm -rf set00.tar

tar xvf set01.tar
rm -rf set01.tar

tar xvf set02.tar
rm -rf set02.tar

tar xvf set03.tar
rm -rf set03.tar

tar xvf set04.tar
rm -rf set04.tar

tar xvf set05.tar
rm -rf set05.tar

tar xvf set06.tar
rm -rf set06.tar

tar xvf set07.tar
rm -rf set07.tar

tar xvf set08.tar
rm -rf set08.tar

tar xvf set09.tar
rm -rf set09.tar

tar xvf set10.tar
rm -rf set10.tar
