
load allNodesData;
clc; close all;
degree=[weak1Nodes{:,5}];


n=50;

names=weak1Nodes(:,3);
[sortedValues,sortIndex] = sort(degree(:),'descend');  %# Sort the values in
                                                  %#   descending order
maxIndex = sortIndex(1:n);  

bestWeights=degree(maxIndex)';
%bestWeights=bestWeights/min(bestWeights);

bestNames=names(maxIndex);



% for i=1:n
%     fprintf('%s: %d \n',bestNames{i},bestWeights(i));
% end

maxDegree=max(degree);

n=100;

distr=hist(degree,length(degree));

figure;
loglog(distr,sort(degree),'LineWidth',2);
xlabel('Degree');
ylabel('Number of nodes');

%legend('Data','Linear fit');


% xlhand = get(gca,'xlabel')
% set(xlhand,'string','X','fontsize',30)

x=log(distr);
y=1:length(distr);
y=log(y);
% hold on;
% plot(y,x,'Color','r');
xlim([1,100]);
badIdx=(x<0);
x(badIdx)=[];
y(badIdx)=[];


p=polyfit(x,y,1);

m = 1000; % number of trendline points (the larger the smoother)
xx = linspace(0, log(maxDegree), m);
yy = polyval(p, xx);

%figure;
hold on;
%scatter(a(:,1), a(:,2));
plot(exp(yy),exp(xx), 'r-','LineWidth',2);

legend('Data','Linear fit');

 figureHandle = gcf;
% %# make all text in the figure to size 14 and bold
 set(findall(figureHandle,'type','text'),'fontSize',14,'fontWeight','bold')