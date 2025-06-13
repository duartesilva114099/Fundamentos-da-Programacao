clear all all
close all
clc
data= load("pts.txt");
x = data(:,1);
y = data(:,2);
n_points = length(x);
fprintf('This program will perform a least-squares fit using %d data points.\n', n_points);

sum_x = 0;
sum_y = 0;
sum_x2 = 0;
sum_xy = 0;
for ii = 1:n_points
    sum_x = sum_x + x(ii);
    sum_y = sum_y + y(ii);
    sum_x2 = sum_x2 + x(ii)^2;
    sum_xy = sum_xy + x(ii) * y(ii);
end

x_bar = sum_x / n_points;
y_bar = sum_y / n_points;
slope = (sum_xy - sum_x * y_bar) / (sum_x2 - sum_x * x_bar);
y_int = y_bar - slope * x_bar;

disp('Regression coefficients for the least−squares line:');
fprintf(' Slope (m) = %8.3f\n', slope);
fprintf(' Intercept (b) = %8.3f\n', y_int);
fprintf(' No. of points = %8d\n', n_points);

plot(x, y, 'bo');
hold on;
xmin = min(x);
xmax = max(x);
ymin = slope * xmin + y_int;
ymax = slope * xmax + y_int;
plot([xmin xmax], [ymin ymax], 'r-', 'LineWidth', 2);
hold off;
title('\bfLeast−Squares Fit');
xlabel('\bf\itx');
ylabel('\bf\ity');
legend('Input data','Fitted line')