DROP TABLE IF EXISTS attendence CASCADE;
DROP TABLE IF EXISTS lesson CASCADE;
DROP TABLE IF EXISTS subject CASCADE;
DROP TABLE IF EXISTS semester CASCADE;
DROP TABLE IF EXISTS field CASCADE;
DROP TABLE IF EXISTS user_roles CASCADE;
DROP TABLE IF EXISTS user_permission CASCADE; 
DROP TABLE IF EXISTS permissions CASCADE;
DROP TABLE IF EXISTS roles CASCADE;
DROP TABLE IF EXISTS users CASCADE;


CREATE TABLE users (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
first_name varchar(80) NOT NULL,
last_name varchar(80) NOT NULL,
email varchar(80)NOT NULL UNIQUE,
phone int NOT NULL
);


CREATE TABLE roles (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
role_name varchar(30) NOT NULL
);


CREATE TABLE permissions (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
perm_name varchar(30) NOT NULL UNIQUE,
view bool NOT NULL,
edit bool NOT NULL, 
delete bool NOT NULL
);


CREATE TABLE user_roles (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
user_id uuid REFERENCES users(UID) NOT NULL,
role_id uuid REFERENCES roles(UID) NOT NULL 
);
	

CREATE TABLE user_permission (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
user_id uuid REFERENCES users(UID),
user_role_id uuid REFERENCES user_roles(UID),
permission_id uuid REFERENCES permissions(UID)
);


CREATE TABLE field (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
capacity int2 NOT NULL
);


CREATE TABLE semester (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
field_id uuid REFERENCES field(UID),
capacity int2
);


CREATE TABLE subject (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
semester_id uuid REFERENCES semester(UID),
number_of_lessons int2,
obligatory bool
);


CREATE TABLE lesson (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
subject_id uuid REFERENCES subject(UID),
start timestamptz NOT NULL,
duration interval NOT NULL,
obligatory bool
);


CREATE TABLE attendence (
UID uuid DEFAULT gen_random_uuid() PRIMARY KEY,
user_id uuid REFERENCES users(UID),
lesson_id uuid REFERENCES lesson(UID),
arrived timestamptz,
departed timestamptz
);

