alpha = 0.72;
phi = alpha;
delta = 0.034;
y_z = 2.5;
job_f = 0.45;
rho = (0.878)^(1/3);
gamma1 = 20;
gamma2 = 1.57;
beta = (0.953)^(1/12);

x=linspace(0,10,1000);
y= 1./(1-(((rho./alpha).*(1-beta.*(1-delta-x.*job_f))./(1-beta.*rho.*(1-delta-x.*job_f./alpha)))./gamma2));
z= 1./(1-(((rho./alpha).*(1-beta.*(1-delta-x.*job_f))./(1-beta.*rho.*(1-delta-x.*job_f./alpha)))./gamma1));
plot(x,y);

hold on;

plot(x,z);
hold off;