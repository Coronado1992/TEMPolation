function [] = f_plot_legend(Title,Legend,xaxis,yaxis,data)

hold on
title(Title)
legend(Legend,data)
ylabel(yaxis)
xlabel(xaxis)
hold off

end

