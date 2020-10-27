% male-female, features are 24-mel filterbank without normalization
% extracted with SPRAAK and mapped to one dimension with PCA
clc
clear all
get(0,'Factory');
set(0,'defaultfigurecolor',[1 1 1]);
fprintf('Data are being loaded...\n');
load male-female
MaleClass=mappedMale;
FemaleClass=mappedFemale;
fprintf('Now, you may type FemaleClass or MaleClass to see the feature values.\n')