CREATE TABLE crash_report(
    user_id integer NOT NULL,
    "timestamp" integer NOT NULL,
    message character varying
);

CREATE TABLE install(
    user_id integer NOT NULL,
    "timestamp" integer NOT NULL
);

CREATE TABLE purchase(
    user_id integer NOT NULL,
    "timestamp" integer NOT NULL,
    sku character varying
);