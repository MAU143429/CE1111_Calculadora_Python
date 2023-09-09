function [x_k, error, k, toc] = open_newton_method (f1, x0, tol, iterMax)

  pkg load symbolic

  f2 = sym(f1);
  f = matlabFunction(f2);


  df = matlabFunction(diff(f2));

  x_k = x0;

  tic;

  for k = 1 : iterMax
    n = f(x_k);
    d = df(x_k);
    if abs(d) < tol
      break;
    endif

    z_k = x_k - n/d;

    error = abs(f(x_k));
    if error < tol
      break;
    endif

    d1 = df((1/4)*(3*x_k + z_k));

    d2 = df((1/2)*(z_k + x_k));

    d3 = df((1/4)*(x_k + 3*z_k));

    x_k_1 = x_k - ((1/(2*d1 - d2 + 2*d3))* 3*n);

    x_k = x_k_1;

  endfor
  toc;
endfunction

