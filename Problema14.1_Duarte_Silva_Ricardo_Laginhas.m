
clear all
close all
clc

x=-1:0.01:3;
y=ones(size(x));
tic
for i = 1:length(x) 
    y(i) =power(x(i),2)-3*x(i) + 2;
end
tempo=toc;
fprintf("o For demora %f segundos\n", tempo);
figure
plot(y)
tic
y= power(x,2) - 3*x +2;
tempo_vec=toc;
figure
plot(y)
fprintf("O vetor demora %f segundos\n", tempo_vec);
