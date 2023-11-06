--Se eleiminan los datos de las tablas
DELETE FROM vehiculo;
DELETE FROM detalle_vehiculo;
DELETE FROM photo_vehiculo;

--Se insertan las carrorecias de los vehiculos 
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('0c2066a4-25fd-4295-8b72-629a99cfda58','SUV');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('8adaec3c-b9cc-4afd-bbeb-8786a5705627','HATCHBACK');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('c4a39a46-f712-46e7-9100-6bdf6a81f971','SEDAN');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('0d74b19a-f499-45d4-88ed-79ba8b0d024b','COUPE');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('c41d6e8e-cfc8-4c50-bfc5-8b368a39b3e7','CITY CAR');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('30d4d6ac-7307-46c6-8bdf-197fa183e63c','COMERCIAL');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('0a2fe34d-2463-4627-a771-b26db3a345ee','CAMIONETA');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('ab0fa403-e01c-4056-995e-455338d21013','DEPORTIVO');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('8ba4381a-7e5d-4b59-ab29-664d21aa8e2c','ELECTRICO');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('008d0a55-e3f5-474f-afb1-eef2964669e6','STATION WAGON');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('116006d6-c755-4d9b-843a-76e28b42ab47','VAN');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('fbc3840a-00a6-4998-ab1c-d1cf197e74d7','No identeficada');