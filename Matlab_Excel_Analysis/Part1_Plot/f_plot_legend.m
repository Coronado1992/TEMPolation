%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                         Master Thesis - Function Complot                                 %
% Created by: B. Sc. Daniel Coronado                                                       %
% Supervised by: M. Sc. Avichal Malhotra                                                   %
% Last update: Februay 2021                                                                %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                    INSTRUCTIONS                                          %
%  This fuction create a title, legend and name the axis on the plot.                      %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [] = f_plot_legend(Title,Legend,xaxis,yaxis,data)
hold on
title(Title)
legend(Legend,data)
ylabel(yaxis)
xlabel(xaxis)
hold off
end

