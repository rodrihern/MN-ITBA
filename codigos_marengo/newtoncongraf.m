function [k,X,E]=newtoncongraf(f,fp,a,b,x0,prec)
  % RECIBE:
  % f: la funcion
  % fp: la derivada de la funcion
  % a: extremo izquierdo del intervalo
  % b: extremo derecho del intervalo
  % x0: valor inicial de la sucesion
  % prec: el epsilon tal que el error sea mas chico (E < epsilon)

  % RETORNA:
  % k: cantidad de pasos hechos
  % X: vector de soluciones en cada paso
  % E: vector de errores en cada paso
    e=1;k=0;X(1)=x0;
    E=[];
    while e>prec
        x=x0-feval(f,x0)/feval(fp,x0);
        e=abs(x-x0);
        E=[E e];
        x0=x;
        k=k+1;
        X=[X x0];
    end

z=a:(b-a)/200:b;
hold on
plot(z,feval(f,z))
plot(z,zeros(size(z)))
P=[X(1) 0]; r=1;
while r<k
    P=[P;[X(r) feval(f,X(r))]];
    P=[P;[X(r+1) 0]];
    r=r+1;
end
plot(P(:,1),P(:,2),'o-')
hold off
