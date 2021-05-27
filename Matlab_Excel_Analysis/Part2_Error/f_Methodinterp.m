function [SensorInterp] = f_Methodinterp(SensorComb,TimeComb,combinations,ncombinations,Time,numDP,Method,Degree)


%%%%%%%%%%%%%%%%%%%%%%%%%%  METHOD 1  %%%%%%%%%%%%%%%%%%%%%%%%%   
if Method == 1
SensorInterp = zeros(ncombinations,numDP);

for i=1:ncombinations  
    x=TimeComb(:,i)';
    y=SensorComb(:,i)';
    vectime = Time(:,1)';
    SensorInterp(i,:) = interp1(x,y,vectime,'linear','extrap');
end
SensorInterp = SensorInterp';     
end

%%%%%%%%%%%%%%%%%%%%%%%%%%  METHOD 2  %%%%%%%%%%%%%%%%%%%%%%%%%     
if Method == 2
SensorInterp = zeros(ncombinations,numDP);
for i=1:ncombinations   
    x=TimeComb(:,i);
    y=SensorComb(:,i); 
    p = polyfit(x,y,Degree);
    SensorInterp(i,:) = polyval(p,Time(:,1));  
end
SensorInterp = SensorInterp';       
end

%%%%%%%%%%%%%%%%%%%%%%%%%%  METHOD 3  %%%%%%%%%%%%%%%%%%%%%%%%%   
if Method == 3
SensorInterp = zeros(ncombinations,numDP);
for i=1:ncombinations  
    x=TimeComb(:,i)';
    y=SensorComb(:,i)';
    vectime = Time(:,1)';
    SensorInterp(i,:) = interp1(x,y,vectime,'nearest','extrap');  %Sprintf(formatSpec,degree)
end
SensorInterp = SensorInterp';  
end

%%%%%%%%%%%%%%%%%%%%%%%%%%  METHOD 4  %%%%%%%%%%%%%%%%%%%%%%%%%  
if Method == 4
SensorInterp = zeros(ncombinations,numDP);
for i=1:ncombinations   
    x=TimeComb(:,i)';
    y=SensorComb(:,i)';
    vectime = Time(:,1)';
    SensorInterp(i,:) = interp1(x,y,vectime,'pchip','extrap');  %Sprintf(formatSpec,degree)    
end
SensorInterp = SensorInterp';
end

%%%%%%%%%%%%%%%%%%%%%%%%%%  METHOD 5  %%%%%%%%%%%%%%%%%%%%%%%%%     
if Method == 5

SensorInterp = zeros(ncombinations,numDP);
for i=1:ncombinations  
    x=TimeComb(:,i)';
    y=SensorComb(:,i)';
    vectime = Time(:,1)';
    SensorInterp(i,:) = interp1(x,y,vectime,'spline','extrap');  %Sprintf(formatSpec,degree)   
end
SensorInterp = SensorInterp';
end

%%%%%%%%%%%%%%%%%%%%%%%%%%  METHOD 6  %%%%%%%%%%%%%%%%%%%%%%%%%     
if Method == 6
SensorInterp = zeros(ncombinations,numDP);
for i=1:ncombinations   
    x=TimeComb(:,i)';
    y=SensorComb(:,i)';
    vectime = Time(:,1)';
    SensorInterp(i,:) = interp1(x,y,vectime,'makima','extrap');  %Sprintf(formatSpec,degree)
    
end
SensorInterp = SensorInterp';
end









end

