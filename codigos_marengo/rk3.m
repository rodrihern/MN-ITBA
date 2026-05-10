function [T,Y]=rk3(f,a,b,ya,N)
  % RECIBE:
  % f: la funcion f tal que y'(t)=f(t,y(t))
  % a: extremo izquierdo del intervalo
  % b: extremo derecho del intervalo
  % ya: condicion inicial en el punto a - y(a)
  % N: la cantidad de pasos tal que luego, h=(b-a)/N

  % RETORNA:
  % T: vector de tiempos o abscisas
  % X: vector de soluciones aproximadas
h=(b-a)/N;
T=zeros(N+1,1);
Y=zeros(N+1,length(ya));
T(1)=a;
Y(1,:)=ya;
for j=1:N
  T(j+1)=T(j)+h;
  K1=h*feval(f,T(j),Y(j,:));
  K2=h*feval(f,T(j)+(h/2),Y(j,:)+(K1/2));
  K3=h*feval(f,T(j)+h,Y(j,:)-K1+2*K2);
  Y(j+1,:)=Y(j,:)+(1/6)*(K1+4*K2+K3);
end
end
