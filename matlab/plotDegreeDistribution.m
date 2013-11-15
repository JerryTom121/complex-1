
load allNodesData;
clc; close all;
degree=[weak1Nodes{:,5}];

[alpha1,xmin1,L1]=plfit(degree);

figure;
subplot(1,4,1);
plplot(degree,xmin1,alpha1,1);

degree=[weak2Nodes{:,5}];

[alpha2,xmin2,L2]=plfit(degree);


subplot(1,4,2);
plplot(degree,xmin2,alpha2,2);

degree=[weak3Nodes{:,5}];

[alpha3,xmin3,L3]=plfit(degree);


subplot(1,4,3);
plplot(degree,xmin3,alpha3,3);


degree=[weak4Nodes{:,5}];

[alpha4,xmin4,L4]=plfit(degree);


subplot(1,4,4);
plplot(degree,xmin4,alpha4,4);


