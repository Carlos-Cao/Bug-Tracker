CREATE TABLE BugTracker(
	id INT NOT NULL AUTO_INCREMENT,
	bug_type VARCHAR(30),
	title VARCHAR(100),
	assigned_to VARCHAR(50),
	priority VARCHAR(30),
	bug_status VARCHAR(30),
	description VARCHAR(300),
	PRIMARY KEY(id)
);