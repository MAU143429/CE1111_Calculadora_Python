function [xk, error, k, tiempo] = biseccion(a, b, func, tol, iterMax)
% Aproximación del cero de la función `func` utilizando el método de la Bisección.
%
% Estructura de llamada: [xk, error, k, tiempo] = biseccion(a, b, func, tol, iterMax)
%
% Parámetros de entrada:
%   a, b: Intervalo [a, b] donde se busca el cero.
%   func: Función a la que se le aproxima el cero.
%   tol: Tolerancia de aproximación.
%   iterMax: Iteraciones máximas a realizar.
%
% Parámetros de salida:
%   xk: Aproximación del cero.
%   error: Error del método dado por |func(xk)|.
%   k: Iteraciones realizadas.
%   tiempo: Tiempo de ejecución en segundos.
%
% Ejemplo de uso:
% [xk, error, k, tiempo] = biseccion(2, 3, '(x/(1+((x/10)-1)*exp(-2e-6*x*60)))-15000', 1e-10, 1000)

pkg load symbolic; % Carga la biblioteca Symbolic de Octave para trabajar con expresiones simbólicas.

% Iniciar el temporizador
tic;

% Convierte la cadena `func` en una función anónima evaluada numéricamente.
f = str2func(['@(x)' func]);

if f(a) * f(b) < 0
    % Verifica si la función tiene un cambio de signo en el intervalo [a, b]. Si no, el método no se puede aplicar.

    for k = 1:iterMax
        % Calcula la próxima aproximación del cero utilizando el método de la bisección.
        xk = (a + b) / 2;

        if f(a) * f(xk) < 0
            % Verifica si la función tiene un cambio de signo en el intervalo [a, xk]. Si es cierto, actualiza `b` con `xk`.
            b = xk;
        else
            a = xk; % Si no hay cambio de signo, actualiza `a` con `xk`.
        end

        error = abs(f(xk)); % Calcula el error absoluto en la aproximación actual del cero.

        if error < tol
            break; % Si el error es menor que la tolerancia, sale del bucle.
        end
    end
else
    % Si no hay cambio de signo inicial en el intervalo [a, b], el método no se puede aplicar.
    xk = 'N/A';
    error = 'N/A';
    k = 'N/A';
    fprintf('No se cumple la condición de Bolzano con los datos dados\n');
end

% Detener el temporizador y calcular el tiempo de ejecución en segundos
tiempo = toc;

% Imprimir los resultados

fprintf('Tiempo de ejecución: %.4f segundos\n', tiempo);

end % Fin de la función biseccion.

%[xk, error, k] = biseccion(60000, 70000, '(x/(1+((x/10)-1)*exp(-2e-6*x*60)))-15000', 1e-10, 100)


