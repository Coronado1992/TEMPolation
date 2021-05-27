function [Error,MaxEach,MaxAll,position,xp,yp] = f_errorcalc(SensorInterp,Sensor)


  Error = round(abs(SensorInterp-Sensor),3);
  MaxEach = max(Error);
  MaxAll = max(max(Error));
  [xp,yp]=find(Error==MaxAll);
  [positionx,positiony]=find(Error==MaxAll);
  position = [positionx,positiony];
  
  
end

