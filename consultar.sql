--Se eleiminan los datos de las tablas
DELETE FROM vehiculo;
DELETE FROM detalle_vehiculo;
DELETE FROM photo_vehiculo;

--Eliminar Tablas
DROP TABLE `carroceria`, `conbustible`, `detalle_vehiculo`, `marca`, `modelo`, `pagina`, `photo_vehiculo`, `vehiculo`;


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
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('4318dc2f-0d9e-4dc4-a54e-45f4866c9aa6','PICK UP');
INSERT INTO `carroceria`(`idCarroceria`, `nombre`) VALUES ('fb040b5f-9442-4d04-a1de-42cf2230c4d5','CAMION');

--Marca de vehiculos 
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('c80afad3-f33b-42c0-a507-ffcf751c4ec7','MAXUS');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('0e381586-9a9a-4204-b2ed-d7c9d9e44c80','SUZUKI');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('b365de2c-6010-4916-89ff-d9e525fe4d7f','HYUNDAI');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('9b247dee-5712-48e9-b408-9b09cf797a23','NISSAN');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('58533aec-2a8e-4143-b261-56f92c0046ff','CHEVROLET');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('64cd2fdf-5a87-4fa3-8099-309b5c1184b5','DFM');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('927c32a2-ffcb-420b-9464-d51924173fa3','MG');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('c126ff3e-0ab6-451d-a77b-2024d66febb2','HONDA');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('c71c7bf3-e503-4c97-a9a9-5748d92c9d87','SSANGYONG');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('d8f02960-4010-4bef-8482-966cb55723d8','BRILLIANCE');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('e9a651be-d51a-4f13-9f68-5074555225f8','DFSK');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('1d77c8e2-7596-405e-bc3f-629dc9da5751','KARRY');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('420c22b8-251f-4ad2-a270-b5b147e98a6d','KIA');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('c25e75ee-ddca-40b1-8b3b-8461f789b1bb','SKODA');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('c2cb25eb-e5b7-4c06-85d5-4daf3e7cc6ca','FORD');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('89ed6a94-bfab-4aa8-87b4-a131d630a9ca','JAC');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('d1764cbd-6c1f-4ffa-bc3b-e9eefcf17565','RENAULT');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('588d8709-7bda-4ffc-9f24-1e91442447c6','CHANGAN');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('6c51c8b6-5a7e-4e29-8665-923e76a4d079','RAM');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('117d62ed-c807-40e3-8fa9-48b635b2cc3b','BAIC');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('fcefec61-1686-44b7-aa30-197878a49dfe','TOYOTA');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('056defc5-3af9-4710-939e-fc0e667f43bb','VOLKSWAGEN');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('9cf6c6d6-da59-4882-b1e2-973b373f462b','PEUGEOT');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('19de0b55-ed06-4ba5-a56d-d1eabfa7a2e2','MAHINDRA');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('49f22f30-f86d-401c-8105-7dec475a8e06','MAZDA');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('0dbe6783-ce93-47a9-ad19-7d4697bd7cd2','CITROEN');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('2cb4f809-b3d1-4154-80df-eee7e0e75ca8','DONGFENG');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('70c16215-55d0-4ade-9bf2-dfaea1169ef2','SUBARU');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('128d7d2b-1647-4932-960f-6fed9e925e42','HAVAL');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('ec0d1df9-f896-4463-bc68-5d064226fe06','JEEP');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('aee707f9-d17e-4b53-a286-1d57db09efa0','OPEL');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('08c6a1fd-82b2-4e1a-8c53-2b3873e1f4ef','HONDA');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('4926e8a6-bfe0-406a-88e4-5c7f9cde2138','KAIYI');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('c5cc2ddf-e795-44bb-8c77-e44526b84c04','KYC');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('a326dd91-2e55-496c-8eeb-b43bdf5c871b','BMW');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('a84b499d-72be-4434-8b45-8189bb6cab45','JETOUR');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('c19c912e-b0de-43fa-8afd-6ab7c3b08713','GEELY');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('caea2d09-520e-490f-a824-12dcb7392c8f','AUDI');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('eda6bd0b-6007-4668-a642-e1c9b311a506','GAC MOTOR');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('3d306049-1031-47af-9375-fb5aea6d7ffc','SSANGYONG');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('98657ae8-ac5d-4446-a17b-0c6258f9161a','VOLVO');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('ce5e3dec-9f2d-4bc5-a8ea-83f2cf211e3a','ALFA ROMEO');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('f8c9cc06-3e1e-46af-86ab-009227400412','Otro');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('284bad23-24a7-493b-b56e-e4661ec9d1fa','CHERY');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('0a00a492-b13e-4a8c-8785-c9fa75f0ba79','JMC');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('82245ae1-5373-4787-9997-398720504a4f','MITSUBISHI');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('02b0ed7e-857d-466e-90b2-e42dc01ebafd','SHINERAY');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('75a43aca-5cd0-4b10-a9d1-04edb352b76d','SEAT');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('1909fba7-eb07-464b-baae-8b9659e9a6d6','GREAT WALL');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('245a0064-304e-49e0-91cc-5a7e2a3f977f','DODGE');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('8386ee18-ec13-41f6-8e0d-1119eb304a02','MAHINDRA');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('a0fdfd77-88ec-4821-aa63-dfa7e604013b','FOTON');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('0bc9689e-a9bc-4222-b809-d5b5ff74bf5a','ZX AUTO');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('a557ea28-7d0e-48b2-a849-ddf50c948bb5','EXEED');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('5a193770-62f5-4f66-84bd-eb2c1b4dc6ed','LEXUS');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('071fc77a-3b30-4ae1-85a0-af893acaf3ff','DS');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('b1582786-be6f-4ace-bc9b-1dcb622cea08','JAGUAR');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('26e02e92-00c5-4b25-a353-a862847bc050','LAND ROVER');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('d528cb27-3131-4d4b-970b-ff0f44c0c884','MINI');
INSERT INTO `marca`(`idMarca`, `nombre`) VALUES ('24a55421-e985-4d47-a260-f8b3765476ef','BYD');

--Insert de paginas
INSERT INTO `pagina`(`idPagina`, `nombrePagina`, `isHabilitada`) VALUES ('2d739c55-400c-43d2-9aa8-bbeb6604a003','Movicenter','1');
INSERT INTO `pagina`(`idPagina`, `nombrePagina`, `isHabilitada`) VALUES ('c2b86d03-3889-4e06-a99c-2d383e832af6','Sergio Escobar','1');
INSERT INTO `pagina`(`idPagina`, `nombrePagina`, `isHabilitada`) VALUES ('91e788a0-4184-4483-9ee3-416aa4db495c','Mercado Libre','0');
INSERT INTO `pagina`(`idPagina`, `nombrePagina`, `isHabilitada`) VALUES ('47bd3441-9a15-4168-a078-45335fa836c5','Cart time','0');
INSERT INTO `pagina`(`idPagina`, `nombrePagina`, `isHabilitada`) VALUES ('229cfb9e-56ea-4879-afd3-da3cfff02c62','Autocosmos','1');

--Insert conbustibles
INSERT INTO `conbustible`(`idConbustible`, `nombreCombustible`) VALUES ('f7131493-10d6-47fb-87e7-0c083bc7bd1b','BENCINA');
INSERT INTO `conbustible`(`idConbustible`, `nombreCombustible`) VALUES ('e3723835-2481-4731-96f9-a9bfc6aba54c','GASOLINA');
INSERT INTO `conbustible`(`idConbustible`, `nombreCombustible`) VALUES ('575c021e-2ee1-451d-af18-ef5221cd95a2','DIESEL');
