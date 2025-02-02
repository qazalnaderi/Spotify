CREATE DATABASE spotify;
\c spotify;

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(15) UNIQUE NOT NULL,
    is_verified boolean NOT NULL DEFAULT false,
    username VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL
);