function [ res ] = regressionFunction( alpha1,alphaStar,xData,x,kernel,rescaleBackFunction )
%REGRESSIONFUNCTION Summary of this function goes here
%   Detailed explanation goes here


n=length(alpha1);

res=0;
for i=1:n
    res=res+(alpha1(i)-alphaStar(i))*kernel(xData(i,:),x);
end

res=rescaleBackFunction(res);

end

