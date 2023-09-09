
function [x_k, error, k, toc] = neta_scott_method (f1, x0, tol, iterMax)

  pkg load symbolic

  f2 = sym(f1);
  f = matlabFunction(f2);

  df = matlabFunction(diff(f2));

  df2 = matlabFunction(diff(diff(f2)));

  x_k = x0;

  A = 2;

  tic;

  for k = 1:iterMax
    n = f(x_k);
    d = df(x_k);
    d2 = df2(x_k);

    if abs(d) < tol
      break;
    endif
    par1 = n/d;

    error = abs(f(x_k));
    if error < tol
      break;
    endif

    x_k_1 = x_k - par1 - (1/(2*d^3 - A*n*d2))*(n^2*d2);

    x_k = x_k_1;
  endfor

  toc;

endfunction
