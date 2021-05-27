function [SensorComb,TimeComb] = f_DeleteData(combinations,ncombinations,Time,Sensor,Missing_data,numDP)

SensorComb = zeros((numDP-Missing_data),ncombinations);
TimeComb = zeros((numDP-Missing_data),ncombinations);

for i=1:ncombinations
    
    delete =  combinations(i,:)';
    VectorTime = Time(:, i);
    VectorSensor = Sensor(:, i);
    
    for m=1:Missing_data     
        VectorSensor(delete(m)) = NaN;
        VectorTime(delete(m))= NaN; 
    end
    
     VectorSensor(any(isnan(VectorSensor),2),:) = [];
     VectorTime(any(isnan(VectorTime),2),:) = [];
        
    SensorComb(:, i) = VectorSensor;
    TimeComb(:, i) = VectorTime;
end

end

