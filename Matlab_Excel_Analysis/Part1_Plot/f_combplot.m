%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                         Master Thesis - Function Complot                                 %
% Created by: B. Sc. Daniel Coronado                                                       %
% Supervised by: M. Sc. Avichal Malhotra                                                   %
% Last update: Februay 2021                                                                %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                    INSTRUCTIONS                                          %
%  This fuction create a plot of the methods.                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function [] = f_combplot(xq,vq,x1,y1,Time,Sensor,Interval,Degree, xq3,vqq,p,s,m,Method1,Method2,Method3,Method4,Method5,Method6,Method7,text)


if Method1 == 1
    hold on
    plot(xq,vq,'m --')
    hold off
end
    
if Method2 == 1
    hold on
    plot(Time, Sensor,'o',x1,y1,'m --')
    hold off
    xlim([1 24])
    ylim([21.5 25])
end
   
if Method3 == 1
    hold on
    plotpoli(Time, Sensor, Interval,Degree)
    hold off    
end
    
if Method4 == 1
    hold on
    plot(xq3,vqq,'m --')
    hold off   
end

if Method5 == 1
    hold on
    plot(0:0.001:length(Time),p,'-')
    hold off  
end
    
if Method6 == 1 
    hold on
    plot(0:0.001:length(Time),s,'-.')
    hold off  
end
    
if Method7 == 1
    hold on
    plot(0:0.001:length(Time),m,'--')
    hold off  
end

title('Combining Interpolation Methods ')
ylabel(text)
xlabel('Time')

end

