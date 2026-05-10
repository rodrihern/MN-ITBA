function [k,X,E] = newtoncongelado(f,fp,x0,prec,maxiter)
  % Variante de newton
  % x_(k+1) = x_k - f(x_k) / f'(x_0)

  % RECIBE:
  % f: la funcion
  % fp: la derivada
  % x0: donde empieza la sucesion
  % prec: el epsilon tal que el error sea mas chico (E < epsilon)
  % maxiter: la cantidad de pasos maximos
  % Recordar que si quiero que pare por el error, le pongo un maxiter grande (Ej: 1000)
  % Si quiero que pare por cantidad de pasos, le pongo una precision chica (Ej: 10^-15)

  % RETORNA:
  % k: cantidad de pasos hechos
  % X: vector de soluciones en cada paso
  % E: vector de errores en cada paso
    e=1;k=0;X=x0;E=[];xn=x0;inic=x0;
    while (e>prec)*(k<=maxiter)
        xn1=xn-feval(f,xn)/feval(fp,x0);
        e=abs(xn1-xn); E=[E;e];
        xn=xn1;
        k=k+1;
        X=[X;xn];
    end
end
