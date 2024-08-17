<h1>To-do-list application in flask</h1>

<h3>Created By Chaudhari Rohan</h3>

<h4>Steps to download and run this project</h4>

<ol start="1">
<li>Download and Extract This Repository</li>
<li>Open command prompt in that folder</li>
<li><p>Install virtualenv if you don't have it</p>  
    
```bash
pip install virtualenv
```

</li>
<li><p>create virtual environment for this project by using</p>

```bash
python -m venv .venv
```
<p align="center">OR</p>

```bash
virtualenv .venv
```
</li>
<li>
<p>Activate virtual environment</p>

```bash
.venv\Scripts\activate
```
</li>
<li>
<p>Install required dependencies</p>
    
```bash
pip install flask flask_mysql
```
</li>
<li>
<p>Run the Project</p>

```bash
python app.py
```
</li>

```SQL
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

</ol>
