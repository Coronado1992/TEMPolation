function [minimum, maximun, avarage] = f_Statistic(Table,Sensor_final)

maximun.Valeu = max(Table.Sensor);
[x1,y1]=find(Table.Sensor==maximum.Valeu);
maximun.position= [x1,y1];

minimum.Valeu = min(Table.Sensor);
[x2,y2]=find(Table.Sensor==minimum.Valeu);
minimum.position=[x2,y2];

avarage.Valeu =mean(Table.Sensor);
[x3,y3]=find(Table.Sensor==avarage.Valeu);
avarage.position=[x3,y3];





end

