function S=simpsoncomp(f,a,b,subint)
  % RECIBE:
  % f: la funcion
  % a: extremo izquierdo del intervalo de integracion
  % b: extremo derecho del intervalo de integracion
  % subint: numero de subintervalos (debe ser un numero par)

  % RETORNA:
  % S: aproximacion por la regla de Simpson compuesta
h=(b-a)/subint;
x=a:h:b;y=zeros(size(x));
for k=1:length(x)
     y(k)=feval(f,x(k));
end
E=y(1)+y(end);
IMP=sum(y(2:2:end-1));
P=sum(y(3:2:end-2));
S=h*(E+4*IMP+2*P)/3;

end
