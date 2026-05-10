function [k,X,E] = biseccion(f,a,b,prec,maxiter)
  % RECIBE:
  % f: la funcion
  % a: extremo izquierdo del intervalo
  % b: extremo derecho del intervalo
  % prec: el epsilon tal que el error sea mas chico (E < epsilon)
  % maxiter: la cantidad de pasos maximos
  % Recordar que si quiero que pare por el error, le pongo un maxiter grande (Ej: 1000)
  % Si quiero que pare por cantidad de pasos, le pongo una precision chica (Ej: 10^-15)

  % RETORNA:
  % k: cantidad de pasos hechos
  % X: vector de soluciones en cada paso
  % E: vector de errores en cada paso
  fa = feval(f,a); fb = feval(f,b);
  err = (b-a)/2; c = (a+b)/2; k=0;
  E=err; X=c;
  while (err > prec)*(k < maxiter)
    fc = feval(f,c);
    if fa*fc > 0
      a = c; fa = fc;
    else
      b = c; fb = fc;
    endif
    err = (b-a)/2;
    E = [E;err];
    c = (a+b)/2;
    X = [X;c];
    k = k+1;
  endwhile
 end
