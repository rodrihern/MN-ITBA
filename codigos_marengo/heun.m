function [T,Y]=heun(f,a,b,ya,N)
  % RECIBE:
  % f: la funcion f tal que y'(t)=f(t,y(t))
  % a: extremo izquierdo del intervalo
  % b: extremo derecho del intervalo
  % ya: condicion inicial en el punto a - y(a)
  % N: la cantidad de pasos tal que luego, h=(b-a)/N

  % RETORNA:
  % T: vector de tiempos o abscisas
  % Y: vector de soluciones aproximadas
h=(b-a)/N;
T=zeros(N+1,1);
Y=zeros(N+1,length(ya));
T(1)=a;
Y(1,:)=ya;
for j=1:N
  T(j+1)=T(j)+h;
  K1=h*feval(f,T(j),Y(j,:));
  K2=h*feval(f,T(j+1),Y(j,:)+K1);
  Y(j+1,:)=Y(j,:)+(K1+K2)/2;
end
end
