function dirScaling(path)
    % Obtener la lista de images en el directorio
    images = dir(fullfile(path, '*.jpg'));
    
    % Iterar sobre cada archivo en el directorio
    for i = 1:numel(images)
        % Obtener el nombre y la ruta completa del archivo actual
        filename = images(i).name;
        filePath = fullfile(path, filename);
        
        % Leer la imagen
        imagen = imread(filePath);
        
        % Escalar la imagen a la mitad
        imagenEscalada = imresize(imagen, 0.5);
        
        % Guardar la imagen escalada con un nuevo nombre
        nuevofilename = ['escalada_' filename];
        nuevafilePath = fullfile(path, nuevofilename);
        imwrite(imagenEscalada, nuevafilePath);
        
        % Mostrar el progreso
        fprintf('Imagen %d de %d escalada y guardada como %s\n', i, numel(images), nuevofilename);
    end
end