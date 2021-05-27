function [xx] = plot_all(SensorComb,TimeComb,combinations,ncombinations,Time,numDP,Degree,Sensor,Missing_data,labelaxis)

for Method=1:6  % MAX 6
[SensorInterp] = f_Methodinterp(SensorComb,TimeComb,combinations,ncombinations,Time,numDP,Method,Degree);
[Error,MaxEach,MaxAll,position,xp,yp] = f_errorcalc(SensorInterp,Sensor);
figure (Method)

%% Ranking
ErrorVecAll = Error(:);
Rank.Max(:,Method) = MaxAll;      % Max Error
Rank.MAE(:,Method) = mae(ErrorVecAll); % Mean absolute error
Rank.RMSE(:,Method) = sqrt(mean(ErrorVecAll.^2));  % Root Mean Squared Error

%% Error Ploting
TimeVec = Time(:);
Error(Error==0) = NaN;
ErrorVec = Error(:);
Vectorplot = [TimeVec,ErrorVec];
Vectorplot(any(isnan(Vectorplot),2),:) = []; 
[Vectorplot,index] = sortrows(Vectorplot,2,'ascend'); 

TimeVec = Vectorplot(:,1);
ErrorVec = Vectorplot(:,2);

c = linspace(1,10,length(TimeVec));
scatter(TimeVec,ErrorVec,15,c,'filled');
colormap(gca,'jet')
axis padded

%% Method Condition
if Method == 1
    mtd = 'Linear';
elseif Method == 2
    mtd = 'Polynomial';
elseif Method == 3    
    mtd = 'Nearest';
elseif Method == 4
    mtd = 'Pchip';
elseif Method == 5
    mtd = 'Spline';
else
    mtd = 'Makima';
end


%% Plot Error
% yyaxis left
% title(['Method:', mtd, ' / Missing data:' , num2str(Missing_data) ])
% xlabel('Time')   
% ylabel('Error')
% yyaxis right
% ylabel(labelaxis)
% 
% xline(xp(1),'--r');
% 
% set(gca,'XGrid','on','YGrid','off')
% set(gca,'XColor','k', 'YColor','k')
% 
% hold on
% plot(Time,Sensor,'+ -')
% 
% save_results_to = "C:\Users\danie\Google Drive\RWTH\RWTH_21_WS\Master Thesis\5-Matlab_Excel\Matlab Tcc\Matlab_Part2_Error1.2\Results";
% savename = join(['pic_Error_Method_', mtd, '_Missing data_' , num2str(Missing_data)]);
% saveas(gcf,fullfile(save_results_to,savename),'png');





xx = 1;
end
xxx= 1;