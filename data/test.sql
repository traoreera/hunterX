CREATE TABLE "information" (
	"id"	INTEGER NOT NULL UNIQUE,
	"user_name"	VARCHAR(100) NOT NULL UNIQUE,
	"gmail"	VARCHAR(100) UNIQUE,
	"passwords"	VARCHAR(100) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

create table "filler_in"(
    "id" INTEGER not null unique unique,
    "name" VARCHAR(100) not null,
    "etat" VARCHAR(100) not null,
    "version" INTEGER not null,
    "description" VARCHAR(200) not null,
    "domaine" VARCHAR(100),
    PRIMARY KEY("id" AUTOINCREMENT)
);