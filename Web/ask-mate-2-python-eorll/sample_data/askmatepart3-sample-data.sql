--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6


-- CREATE NEW TABLE FOR USERS
CREATE TABLE users (
    id serial NOT NULL,
    nick text,
    email text UNIQUE,
    pw_hash varchar,
    birth_date timestamp without time zone,
    reputation integer,
    access_level varchar,
    join_date timestamp without time zone
);


-- ADD NEW COLUMNS owner_id FOR EXISTING TABLES
ALTER TABLE question
    ADD COLUMN owner_id integer not null default 1;

ALTER TABLE answer
    ADD COLUMN owner_id integer not null default 1;

ALTER TABLE comment
    ADD COLUMN owner_id integer not null default 1;


-- BEFORE BELOW QUERIES SET CORRECT TABLE OWNER IN PGADMIN
-- ADD DEFAULT USER
INSERT INTO users (nick, email, pw_hash, birth_date, reputation, access_level, join_date)
VALUES ('user_nick',
        'email@email.com',
        '$2b$12$s8Qmmgn4m6eDXuq1KTdgI.Y2yF6kfoXKBl9xk0C6Bj7Z7FxSTkEsG',
        (SELECT CURRENT_TIMESTAMP(0)),
        0,
        'user',
        (SELECT CURRENT_TIMESTAMP(0))
        );


-- ADD CONSTRAINTS
ALTER TABLE IF EXISTS ONLY public.users
    DROP CONSTRAINT IF EXISTS pk_user_id CASCADE;
ALTER TABLE ONLY users
    ADD CONSTRAINT pk_user_id PRIMARY KEY (id);

ALTER TABLE IF EXISTS ONLY public.question
    DROP CONSTRAINT IF EXISTS fk_owner_id CASCADE;
ALTER TABLE ONLY question
    ADD CONSTRAINT fk_owner_id FOREIGN KEY (owner_id) REFERENCES users(id);

ALTER TABLE IF EXISTS ONLY public.answer
    DROP CONSTRAINT IF EXISTS fk_owner_id CASCADE;
ALTER TABLE ONLY answer
    ADD CONSTRAINT fk_owner_id FOREIGN KEY (owner_id) REFERENCES users(id);

ALTER TABLE IF EXISTS ONLY public.comment
    DROP CONSTRAINT IF EXISTS fk_owner_id CASCADE;
ALTER TABLE ONLY comment
    ADD CONSTRAINT fk_comment_id FOREIGN KEY (owner_id) REFERENCES users(id);
