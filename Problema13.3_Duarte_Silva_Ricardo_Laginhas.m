

clear all
close all
clc


x1= 0:0.1:10;
x2= 0:0.01:10;
y1=sin(x1);
y2=sin(x2);
figure
scatter(x2,y2,"g")
hold on 
scatter(x1,y1,"filled","r")
xlabel("X")
ylabel("Y")
hold off
legend('0.01','0.1')
grid on
