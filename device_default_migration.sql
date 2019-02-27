-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."device" (
    "id" numeric NOT NULL,
    "longatuide" numeric,
    "latitude" numeric,
    "name" varchar(40),
    "core_id" numeric,
    PRIMARY KEY ("id")
);

INSERT INTO "public"."device" ("id", "longatuide", "latitude", "name", "core_id") VALUES ('1', '-80.2076495', '25.7792277', 'Spring Garden Point Park', '400036001751353338363036'),
('2', '-80.233346', '25.727345', 'City of Miami Town Hall', '400036001751353338363037'),
('3', '-80.1275897', '25.8864952', 'Surfside Park', '400036001751353338363038');
