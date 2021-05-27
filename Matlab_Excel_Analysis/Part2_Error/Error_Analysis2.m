%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                        Master Thesis - Error with combination (Part 2)                   %
% Created by: B. Sc. Daniel Coronado                                                       %
% Supervised by: M. Sc. Avichal Malhotra                                                   %
% Last update: Februay 2021                                                                %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                    INSTRUCTIONS                                          %
% The goal of this file is to compare the error between the the number of missing points   %
% in each interpolation methods (this will be a fast way to eliminate the worst scenario). %
% *Each line has a comment with a small description.                                       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%======= Clean all variables================================================================
clc,clear all,close all;                 %clear all variables and close all figure.
%===========================================================================================

%======= Original Data File =======
%======= Reading Excel data ================================================================
readfile = "file1.xlsx"; 
Analyze = "Sheet3";          %Choose humidity or temperatura (internal/external).
%Sheet 1 = Inside Temp.
%Sheet 2 = Inside Hum.
%Sheet 3 = Outside Temp.
%Sheet 4 = Outside Hum.

%======= Choose Analyze and Missing data =======
Missing_data = 4;              %Number of missing data to implement in the file.

if readfile == "file1.xlsx" & Analyze == "Sheet1"
    labelaxis = "Inside Temp. (file 1)";
elseif readfile == "file1.xlsx" & Analyze == "Sheet2"
    labelaxis = "Inside Hum. (file 1)";
elseif readfile == "file1.xlsx" & Analyze == "Sheet3"
    labelaxis = "Outside Temp. (file 1)";
elseif readfile == "file1.xlsx" & Analyze == "Sheet4"
    labelaxis = "Outside Hum. (file 1)";
elseif readfile == "file2.xlsx" & Analyze == "Sheet1"
    labelaxis = "Inside Temp. (file 2)";
elseif readfile == "file2.xlsx" & Analyze == "Sheet2"
    labelaxis = "Inside Hum. (file 2)";
elseif readfile == "file2.xlsx" & Analyze == "Sheet3"
    labelaxis = "Outside Temp. (file 2)";
else
    labelaxis = "Outside Hum. (file 2)";  
end   
    
Degree = 3;      %Choose the function to be plot.
Excel= xlsread(readfile, Analyze);
[numDP,Time,Sensor,C,Backup,text] = f_ReadingFile(Excel,Analyze);
%===========================================================================================



%======= Combination of missing data =======
[ncombinations,combinations] = f_Combination(numDP,Missing_data);
%======= Extracting orginal time and temperature =======
for i=1:ncombinations
    for j=1:Missing_data
        Table.SensorDeleted(i,j) = Sensor(combinations(i,j),1);
        Table.TimeDeleted(i,j) = Time(combinations(i,j),1);
    end
end
%======= New curve with missing points =======
Sensor = repmat(Sensor,1,ncombinations);
Time = repmat(Time,1,ncombinations);
[SensorComb,TimeComb] = f_DeleteData(combinations,ncombinations,Time,Sensor,Missing_data,numDP);
%MissingValeus.SensorComb1 = SensorComb;



[xx] = plot_all(SensorComb,TimeComb,combinations,ncombinations,Time,numDP,Degree,Sensor,Missing_data,labelaxis);
close all


%======= Plotting =======
% for Method=1:6
% [SensorInterp] = f_Methodinterp(SensorComb,TimeComb,combinations,ncombinations,Time,numDP,Method,Degree);
% [Error,MaxEach,MaxAll,position,xp,yp] = f_errorcalc(SensorInterp,Sensor);
% figure (Method)
% 
% TimeVec = Time(:);
% Error(Error==0) = NaN;
% ErrorVec = Error(:);
% Vectorplot = [TimeVec,ErrorVec];
% Vectorplot(any(isnan(Vectorplot),2),:) = []; 
% [Vectorplot,index] = sortrows(Vectorplot,2,'ascend'); 
% 
% TimeVec = Vectorplot(:,1);
% ErrorVec = Vectorplot(:,2);
% 
% c = linspace(1,10,length(TimeVec));
% scatter(TimeVec,ErrorVec,15,c,'filled');
% colormap(gca,'jet')
% axis padded
%     
% if Method == 1
%     mtd = 'Linear';
% elseif Method == 2
%     mtd = 'Polynomial';
% elseif Method == 3    
%     mtd = 'Nearest';
% elseif Method == 4
%     mtd = 'Pchip';
% elseif Method == 5
%     mtd = 'Spline';
% else
%     mtd = 'Makima';
% end
% 
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
% save_results_to = "C:\Users\danie\Google Drive\RWTH\RWTH_21_WS\Master Thesis\5-Matlab_Excel\Matlab Tcc\Matlab_Part2_Error2";
% savename = join(['pic_Error_Method_', mtd, '_Missing data_' , num2str(Missing_data)]);
% saveas(gcf,fullfile(save_results_to,savename),'png');
% 
% end


