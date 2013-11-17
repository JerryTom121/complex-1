clc;clear; close all;

load boxOfficeRegression;


money=[boxOffice{:,2}];

posTweets=[timeDataForRegression{:,2}];
negTweets=[timeDataForRegression{:,3}];

%rescale variables to be with zero mean and from the interval [0,1]

% find mean
m=mean(money);

% subtract mean
money=money-m;

%find min element
%minMoney=min(money);

% make data from [0,...)
%money=money-minMoney;

% rescale data to be in the interval [-1,1];
maxMoney=max(abs(money));

money=money/maxMoney;


% rescale back transformation
rescaleBack=@(x) (x*maxMoney)+m;

money=money';

kernel=@(X,Y) X*Y';


x=[posTweets;negTweets];
x=x';

n=length(x);

for i=1:n
    for j=1:n
        
        K(i,j)=kernel(x(i,:),x(j,:));
    end
end


%K=pdist2(x,x,kernel);




epsilon=0.01;

C=1;

[al1,alStar]=svrDual(K,money,C,epsilon);

reg=@(newX) regressionFunction(al1,alStar,x,newX,kernel,rescaleBack);
