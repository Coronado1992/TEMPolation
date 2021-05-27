%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                         Master Thesis - Function Complot                                 %
% Created by: B. Sc. Daniel Coronado                                                       %
% Supervised by: M. Sc. Avichal Malhotra                                                   %
% Last update: Februay 2021                                                                %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                    INSTRUCTIONS                                          %
%  This fuction read the excel file and create the main variables.                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [numDP,Time,Sensor,text] = f_ReadingFile(Excel,Analyze)

[lines, columns] = size(Excel);
numDP = lines;
Time = Excel(:,1);
Sensor = Excel(:,2); 

if Analyze == "Sheet1"
    text = "Inside Temp";
elseif Analyze == "Sheet2"
    text = "Inside Humidity";
elseif Analyze == "Sheet3"
    text = "Outside Temp";    
else 
    text = "Outside Humidity";     
end    
end
