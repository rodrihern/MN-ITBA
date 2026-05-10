function [k,X,E]=puntofijocongraf(g,a,b,x0,prec)
  % RECIBE:
  % g: la funcion tal que x_despejada = g
  % a: extremo izquierdo del intervalo
  % b: extremo derecho del intervalo
  % x0: valor inicial de la sucesion
  % prec: el epsilon tal que el error sea mas chico (E < epsilon)

  % RETORNA:
  % k: cantidad de pasos hechos
  % X: vector de soluciones en cada paso
  % E: vector de errores en cada paso
  e=100;k=0;X(1)=x0; E=[];
  while e>prec
    x=feval(g,x0);
    e=abs(x-x0);
    E=[E e];
    x0=x;
    k=k+1;
    X=[X;x0];
  endwhile

  z=a:(b-a)/200:b;
  plot(z(:),z(:),z(:),feval(g,z(:)))
  hold on
  P=[X(1) a];
  for i=1:k-1
    P=[P;[X(i) X(i+1);X(i+1) X(i+1)]];
  endfor

  for j=1:k
    plot(P(j,1),P(j,2),'o')
    plot(P(j,1),a,'x')
    pause(0.5)
  endfor

  plot(P(:,1),P(:,2))
  hold off
 end
