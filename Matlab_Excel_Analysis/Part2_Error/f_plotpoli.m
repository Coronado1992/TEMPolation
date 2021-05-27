function [] = f_plotpoli(Time, Sensor, Interval,Degree)

Timex = reshape(Time, [], Interval);
Sensory = reshape(Sensor, [], Interval);

%Random Color
cm{1}='r';
cm{2}='b';
cm{3}='m';
cm{4}='r';
cm{5}='c';
cm{6}='g';
cm{7}='w';
cm{8}='k';
cm{9}='r';

for i=1:Interval
hold on
    fitresult = fit(Timex(:,i), Sensory(:,i), "poly"+Degree);  
    
    tstart = Timex(1,i);
    tend = Timex(length(Time)/Interval,i); 
    xlim([tstart tend+1]);
    
    plot(fitresult,cm(i)+ "--")
 
    xlim([1 length(Time)])
    ylim([22 25.5])
hold off
end

title("Polynomial segment order " + Degree)
legend('Data Points',Interval + " Polynomial segment ")

end

