function [xk, error, k] = false_position(a, b, func, tol, iterMax)
% La función false_position calcula una aproximación de una función utilizando el método de la falsa posición.
% Argumentos de entrada:
%   a: Punto inicial del intervalo.
%   b: Punto final del intervalo.
%   func: La función cuya raíz se desea encontrar en formato de cadena.
%   tol: Tolerancia para detener el algoritmo cuando el error es menor que este valor.
%   iterMax: Número máximo de iteraciones permitidas.
% Argumentos de salida:
%   xk: Aproximación de la raíz.
%   error: Error absoluto en la aproximación de la raíz.
%   k: Número de iteraciones realizadas.

pkg load symbolic; % Carga la biblioteca Symbolic de Octave para trabajar con expresiones simbólicas.

f = str2func(['@(x)' func]); % Convierte la cadena de la función en una función anónima evaluada numéricamente.

% Iniciar el temporizador
tic;

if f(a) * f(b) < 0
    % Verifica si la función tiene un cambio de signo en el intervalo [a, b]. Si no, el método no se puede aplicar.

    for k = 1:iterMax % Inicia un bucle que iterará hasta alcanzar el número máximo de iteraciones especificado.

        xk = b - (b - a) / (f(b) - f(a)) * f(b); % Calcula el próximo valor de xk utilizando el método de la falsa posición.

        if f(a) * f(xk) < 0
            % Verifica si la función tiene un cambio de signo en el intervalo [a, xk]. Si es cierto, actualiza b con xk.
            b = xk;
        else
            a = xk; % Si no hay cambio de signo, actualiza a con xk.
        end

        error = abs(f(xk)); % Calcula el error absoluto en la aproximación actual de la raíz.

        if error < tol
            break; % Si el error es menor que la tolerancia, sale del bucle.
        end

    end % Fin del bucle for.

else
    % Si no hay cambio de signo inicial en el intervalo [a, b], el método no se puede aplicar.
    xk = 'N/A';
    error = 'N/A';
    k = 'N/A';
    fprintf('No cumple con el Teorema de Bolzano, por lo que no se puede resolver\n');
end

% Detener el temporizador y calcular el tiempo de ejecución en segundos
tiempo = toc;

% Imprimir el tiempo de ejecución
fprintf('Tiempo de ejecución: %.4f segundos\n', tiempo);

end % Fin de la función false_position.

% Llama a la función false_position con los valores de entrada
%[xk, error, k] = false_position(60000, 70000, '(x/(1+((x/10)-1)*exp(-2e-6*x*60)))-15000', 1e-10, 100);



