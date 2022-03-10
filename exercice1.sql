/*Creation de la base de donnee exercice1*/
CREATE DATABASE IF NOT EXISTS exercice1;

/*Se connecter à la bd exercice1*/
USE exercice1;

/*creation de la table references*/
CREATE TABLE reference(
  id_ref INT AUTO_INCREMENT PRIMARY KEY,
  prix FLOAT DEFAULT 0
);

/*creation de la table pieces dans la bd exercice1*/
CREATE TABLE pieces (
  id_piece INT AUTO_INCREMENT PRIMARY KEY,
  categories VARCHAR(100),
  dates DATE,
  id_ref INT,
  FOREIGN KEY (id_ref) REFERENCES reference(id_ref)
);

/*creation de la table vehicule*/
CREATE TABLE vehicules (
  id_vehicule INT AUTO_INCREMENT PRIMARY KEY,
  marque VARCHAR(30),
  annee YEAR,
  modele VARCHAR(30)
);

/*creation de la table correspond*/
CREATE TABLE correspond (
  id_piece int,
  id_vehicule int,
  FOREIGN KEY (id_piece) REFERENCES pieces(id_piece),
  FOREIGN KEY (id_vehicule) REFERENCES vehicules(id_vehicule),
  PRIMARY KEY(id_piece, id_vehicule)
);
