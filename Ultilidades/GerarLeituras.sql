DELIMITER $$
CREATE PROCEDURE GERARDADOS(Num INT)
BEGIN
    DECLARE counter INT DEFAULT 1;
    delete from LeituraMeteorologica where IDLeituraMeteorologica <> 0;
    WHILE counter <= Num DO
        SET counter = counter + 1;
		INSERT INTO `RAIM`.`LeituraMeteorologica`
		(
			`IDEstacaoMeteorologica`,
			`Temperatura`,
			`Umidade`,
			`Pressao`,
			`DataLeitura`
        )
		VALUES
		(
			1,
			(SELECT FLOOR(RAND()*(30))+15),
			(SELECT FLOOR(RAND()*(70))+35),
			(SELECT FLOOR(RAND()*(400))+500),now()
        );
    END WHILE;
END$$
DELIMITER ;

CALL GERARDADOS(100);

