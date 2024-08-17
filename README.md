<h1>To-do-list application in flask</h1>

<h3>Created By Chaudhari Rohan</h3>

<h4>Steps to download and run this project</h4>

<ul>
<li starts='1'></li>

```SQL
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
</ul>
