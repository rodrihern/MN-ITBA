function [k,X,E] = newton(f,fp,x0,prec,maxiter)
  % RECIBE:
  % f: la funcion
  % fp: la derivada de la funcion
  % x0: valor inicial de la sucesion
  % prec: el epsilon tal que el error sea mas chico (E < epsilon)
  % maxiter: la cantidad de pasos maximos
  % Recordar que si quiero que pare por el error, le pongo un maxiter grande (Ej: 1000)
  % Si quiero que pare por cantidad de pasos, le pongo una precision chica (Ej: 10^-15)

  % RETORNA:
  % k: cantidad de pasos hechos
  % X: vector de soluciones en cada paso
  % E: vector de errores en cada paso
  e=1;k=0;X=x0;E=[];xn=x0;
  while (e>prec)*(k<=maxiter)
    xn1=xn-feval(f,xn)/feval(fp,xn);
    e=abs(xn1-xn); E=[E;e];
    xn=xn1;
    k=k+1;
    X=[X;xn];
  end
end
