% clc;clear;close all;
%
%
% load allNodesData;
% load wordSentiment;



mod1=[weak1Nodes{:,11}];
mod2=[weak2Nodes{:,11}];
mod3=[weak3Nodes{:,11}];
mod4=[weak4Nodes{:,11}];

h1=hist(mod1,length(unique(mod1)));
h2=hist(mod2,length(unique(mod2)));
h3=hist(mod3,length(unique(mod3)));
h4=hist(mod4,length(unique(mod4)));


pos=[wordSentiments{:,2}];
neg=[wordSentiments{:,3}];
tot=pos+neg;

names=wordSentiments(:,1);


% fix community ( or find community based on the word of interest)

community=1;

idx=(mod1==community);

com=weak1Nodes(idx,:);

threshold=5;

m1=0;
c=1;
for i=1:length(com)
    name=com{i,3};
    index=find(ismember(names,name));
    
    if (tot(index)>threshold)
        m1(c)=pos(index)/tot(index);
        c=c+1;
    end
    
end

c=1;
for index=1:length(weak1Nodes)
    if (tot(index)>threshold)
        m2(c)=pos(index)/tot(index);
        c=c+1;
    end
end
