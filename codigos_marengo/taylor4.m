function [T,Y]=taylor4(f,fp,fpp,fppp,a,b,ya,N)
  % RECIBE:
  % f: la funcion f tal que y'(t)=f(t,y(t))
  % fp: primera derivada
  % fpp: segunda derivada
  % fppp: tercera derivada
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
    K2=h^2/2*feval(fp,T(j),Y(j,:));
    K3=h^3/6*feval(fpp,T(j),Y(j,:));
    K4=h^4/24*feval(fppp,T(j),Y(j,:));
    Y(j+1,:)=Y(j,:)+K1+K2+K3+K4;
  end
