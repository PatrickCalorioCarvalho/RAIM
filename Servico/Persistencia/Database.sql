create database RAIM;
use RAIM;

create table EstacaoMeteorologica (
	IDEstacaoMeteorologica int not null,
    Nome varchar(50) not null,
    Lat varchar(20),
    Log varchar(20),
	PRIMARY KEY (IDEstacaoMeteorologica)
);
insert into EstacaoMeteorologica(IDEstacaoMeteorologica,Nome) values (1,'Teste');
create table LeituraMeteorologica (
	IDLeituraMeteorologica int not null auto_increment,
    IDEstacaoMeteorologica int not null,
    Temperatura Float,
    Umidade Float,
    Pressao Float,
	DataLeitura datetime not null,
    PRIMARY KEY (IDLeituraMeteorologica),
    FOREIGN KEY (IDEstacaoMeteorologica) REFERENCES EstacaoMeteorologica(IDEstacaoMeteorologica)
);
