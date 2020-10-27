function testGaussianbinary(dim,nc,numsample)
% clc
% dim=2;
% nc= 1;
% numsample=500;
if numsample==400
load a-i-uw-400.mat
elseif numsample==800
        load a-i-uw-800.mat
else
    error(sprintf('Number of samples can be only 400 or 800.'));
end
%% PCA
[T,score,latent]=pca(ALLtrain');
mappedALLtrain= ALLtrain' * T(:,1:dim);
mappedALLtest= ALLtest' * T(:,1:dim);
for i=1:length(trainclass)
   mappedtrainclass{i}= trainclass{i}' * T(:,1:dim); 
   mappedtestclass{i}= testclass{i}' * T(:,1:dim); 
end
group=[ones(1,numsample) 2*ones(1,numsample)];
group=[ones(1,numsample) 2*ones(1,numsample) 3*ones(1,numsample)];

for i=1:length(trainclass) 
classgmm{i}=fitgmdist(mappedtrainclass{i},nc,'CovType','diag','Regularize',0,'Replicates',20,'Options',statset('MaxIter',500));
end
%% TEST
group=[ones(1,size(testclass{i},2)) 2*ones(1,size(testclass{i},2))];
group=[ones(1,size(testclass{i},2)) 2*ones(1,size(testclass{i},2)) 3*ones(1,size(testclass{i},2))];
numclass=max(unique(group));
test_data=mappedALLtest;
label_test=group;
obj=classgmm;
 for j=1:numclass
    curr_test=test_data(label_test==j,:);
    global_output_labelmat=zeros(numclass,size(curr_test,1));
        
            for classnum=1:length(obj)
                global_output_labelmat(classnum,:)= mean((log(pdf(obj{classnum},curr_test))),2);

            end             

  [~,index_test]=max(global_output_labelmat());
           S(j) = sum(index_test==[j]); %/length(curr_test))*100;
          accuracy=100 * sum(S)/length(label_test);
 end
fprintf('Dimension: %d, Number of Gaussian components: %d \n',dim,nc)
fprintf('Total Accuracy: %f \n', accuracy)