CREATE TABLE "employees" (
    "id" serial PRIMARY KEY,
    "name" varchar,
    "username" varchar,
    "password_hash" varchar,
    "gender" varchar,
    "birthdate" date
);

CREATE TABLE "doctors" (
    "id" serial PRIMARY KEY,
    "name" varchar,
    "username" varchar,
    "password_hash" varchar,
    "gender" varchar,
    "birthdate" date,
    "work_start_time" time without time zone,
    "work_end_time" time without time zone
);

CREATE TABLE "patients" (
    "id" serial PRIMARY KEY,
    "name" varchar,
    "gender" varchar,
    "birthdate" varchar,
    "no_ktp" varchar,
    "address" text,
    "vaccine_type" varchar,
    "vaccine_count" int
);

CREATE TYPE appointment_status as ENUM ('IN_QUEUE','DONE','CANCELLED');
CREATE TABLE "appointments" (
    "id" serial PRIMARY KEY,
    "patient_id" int,
    "doctor_id" int,
    "datetime" timestamp without time zone,
    "status" appointment_status,
    "diagnose" text,
    "notes" text
);

ALTER TABLE "appointments"
ADD FOREIGN KEY ("patient_id") REFERENCES "patients" ("id");
ALTER TABLE "appointments"
ADD FOREIGN KEY ("doctor_id") REFERENCES "doctors" ("id");