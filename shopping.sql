create database spesa;
use spesa;

create table utenti(
id int auto_increment primary key,
nome varchar(15) unique
);

create table spesa (
id_utente int,
oggetto varchar(15),
foreign key (id_utente) references utenti(id),
unique(id_utente,oggetto)
);



