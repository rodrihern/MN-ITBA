function [k,X,E]=jacobi(A,Y,X0,prec,maxiter)
  % RECIBE:
  % A: la matriz del sistema de ecuaciones de n x n.
  % Y: el vector columna n x 1 de los terminos independientes.
  % X0: el vector inicial con el que comienza el metodo iterativo.
  % prec: el epsilon tal que el error sea mas chico (E < epsilon)
  % maxiter: la cantidad de pasos maximos
  % Recordar que si quiero que pare por el error, le pongo un maxiter grande (Ej: 1000)
  % Si quiero que pare por cantidad de pasos, le pongo una precision chica (Ej: 10^-15)

  % RETORNA:
  % k: cantidad de pasos hechos
  % X: vector de soluciones en cada paso
  % E: vector de errores en cada paso
[n,m]=size(A);
e=1;k=0;
X=[X0];
X0=X0(:);Y=Y(:);
E=[];
% Se escala cada ecuacion por el termino diagonal...
for i=1:n
  c=A(i,i);
  for j=1:n
      A(i,j)=A(i,j)/c;
  end
      Y(i)=Y(i)/c;
end

while((e>prec)*(k<maxiter))
  x=X0+(Y-A*X0);
  X=[X x];
  e=max(abs(x-X0));
  E=[E e];
  k=k+1;
  X0=x;
end

end
