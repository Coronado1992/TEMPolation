function [numDP,Time,Sensor,C,Backup,text] = f_ReadingFile(Excel,Analyze)

[lines, columns] = size(Excel);
numDP = lines;
Time = Excel(:,1);
Backup.Time = Excel(:,1);
C = zeros(numDP,1);
Sensor = Excel(:,2); 
Backup.Sensor = Excel(:,2);

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
