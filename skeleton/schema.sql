CREATE TABLE IF NOT EXISTS Sailors (
  sid SERIAL8 PRIMARY KEY,
  name TEXT,
  age BIGINT,
  experience BIGINT -- years of experience
);

CREATE TABLE IF NOT EXISTS Boats (
  bid SERIAL8 PRIMARY KEY,
  name TEXT,
  color TEXT
);

CREATE TABLE IF NOT EXISTS Voyages (
  sid BIGINT NOT NULL,
  bid BIGINT NOT NULL,
  date_of_voyage DATE NOT NULL,
  PRIMARY KEY(sid, bid, date_of_voyage)
);
