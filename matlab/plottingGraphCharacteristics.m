clc;clear;close all;

load graphData;



diameter=[graphCharacteristics(:).diameter];
avgPathLenght=[graphCharacteristics(:).avgPathLength];
avgClusteringCoefficient=[graphCharacteristics(:).avgClusteringCoefficient];

time=1:4;

h=figure;
subplot(1,2,1);

plot(time,diameter,'Color','b','LineWidth',2);
hold on;
plot(time,avgPathLenght,'Color','r','LineWidth',2);
ylim([0,8]);
legend('Diameter','Average Path Length');
xlabel('Week');

P = get(h,'Position');
set(h,'Position',[1,100,200,300]);

subplot(1,2,2);

plot(time,avgClusteringCoefficient,'LineWidth',2);
legend('Average Clustering Coefficient');
xlabel('Week');


figureHandle = gcf;
%# make all text in the figure to size 14 and bold
set(findall(figureHandle,'type','text'),'fontSize',14,'fontWeight','bold')