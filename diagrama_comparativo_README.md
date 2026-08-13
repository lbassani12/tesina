% =====================================================================
%  Diagrama comparativo: Microsoft Azure (Pipes and Filters)
%  vs Framework de la Tesina (Tubos y Filtros)
%  (Figura propuesta para Cap. 3, Sección 3.2.10)
%
%  Source of truth del diagrama. Para regenerar PNG y PDF, subí el
%  archivo diagrama_comparativo.puml a https://www.plantuml.com/plantuml/uml/
%  o ejecutá localmente:
%      java -jar plantuml.jar diagrama_comparativo.puml
%      pdftoppm -png -singlefile -r 150 diagrama_comparativo.pdf Diagrama-Comparativo
%
%  Convención de colores:
%    Verde   (#D8E8D8) : componente estructuralmente EQUIVALENTE en ambas
%    Celeste (#D0E8F0) : componente EXCLUSIVO de Azure (Blob Storage,
%                                          Competing Consumers)
%    Amarillo(#F0E0B0) : filtro EXTENDIDO en la tesina (Verificación con
%                                          compuerta blanda)
%    Rosa    (#F0B0B0) : componente EXCLUSIVO de la tesina (sintonizadores)
%    Línea punteada    : correspondencia estructural entre componentes
% =====================================================================
