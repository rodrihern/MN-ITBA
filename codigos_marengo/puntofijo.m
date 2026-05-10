function [k,X,E] = puntofijo(g,x0,prec,maxiter)
  % RECIBE:
  % g: la funcion tal que x_despejada = g
  % x0: valor inicial de la sucesion
  % prec: el epsilon tal que el error sea mas chico (E < epsilon)
  % maxiter: la cantidad de pasos maximos
  % Recordar que si quiero que pare por el error, le pongo un maxiter grande (Ej: 1000)
  % Si quiero que pare por cantidad de pasos, le pongo una precision chica (Ej: 10^-15)

  % RETORNA:
  % k: cantidad de pasos hechos
  % X: vector de soluciones en cada paso
  % E: vector de errores en cada paso
X=[x0]; E=[];
for k=1:maxiter
	p=feval(g,x0);
  err=abs(p-x0);
  E=[E;err];
	x0=p;
	X=[X; x0];
        if (err<prec)
              break;
        end
end

if k == maxiter
disp('numero maximo de iteraciones excedido')
end
