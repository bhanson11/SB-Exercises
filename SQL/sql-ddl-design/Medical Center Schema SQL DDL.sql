-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "DOCTORS" (
    "doctor_id" int   NOT NULL,
    "first_name" text   NOT NULL,
    "last_name" text   NOT NULL,
    "specialty" text   NOT NULL,
    CONSTRAINT "pk_DOCTORS" PRIMARY KEY (
        "doctor_id"
     )
);

CREATE TABLE "PATIENTS" (
    "patient_id" int   NOT NULL,
    "first_name" text   NOT NULL,
    "last_name" text   NOT NULL,
    "birthdate" date,
    "insurance" text,
    "diagnoses" int   NOT NULL,
    CONSTRAINT "pk_PATIENTS" PRIMARY KEY (
        "patient_id"
     )
);

CREATE TABLE "VISITS" (
    "visit_id" int   NOT NULL,
    "doctor_id" int   NOT NULL,
    "patient_id" int   NOT NULL,
    "visit_date" date   NOT NULL,
    "diagnoses" int   NOT NULL,
    "medications_prescribed" text   NOT NULL,
    CONSTRAINT "pk_VISITS" PRIMARY KEY (
        "visit_id"
     )
);

CREATE TABLE "DIAGNOSES" (
    "diagnosis_id" int   NOT NULL,
    "disease_name" text   NOT NULL,
    CONSTRAINT "pk_DIAGNOSES" PRIMARY KEY (
        "diagnosis_id"
     )
);

ALTER TABLE "PATIENTS" ADD CONSTRAINT "fk_PATIENTS_diagnoses" FOREIGN KEY("diagnoses")
REFERENCES "DIAGNOSES" ("diagnosis_id");

ALTER TABLE "VISITS" ADD CONSTRAINT "fk_VISITS_doctor_id" FOREIGN KEY("doctor_id")
REFERENCES "DOCTORS" ("doctor_id");

ALTER TABLE "VISITS" ADD CONSTRAINT "fk_VISITS_patient_id" FOREIGN KEY("patient_id")
REFERENCES "PATIENTS" ("patient_id");

ALTER TABLE "VISITS" ADD CONSTRAINT "fk_VISITS_diagnoses" FOREIGN KEY("diagnoses")
REFERENCES "DIAGNOSES" ("diagnosis_id");

