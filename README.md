# Chatter

> Insanely fast messaging using <a href="https://rethinkdb.com">rethinkdb</a> realtime native database.

---

### Installation

> Before running commands below make sure you have <a href="https://www.docker.com">docker</a> up and running.

> On Windows make sure <u>you have "make"</u> on your PATH variable (install it first using e.g. <a href="https://chocolatey.org">choco</a> package manager via `choco install make`)

0. `docker-compose up -d`
1.  `make install` (installing the necessary python libs)
2.  `make run` (fire up the ui and service)

 is available @ <a href="http://127.0.0.1:2222">localhost:2222</a>

---

### Workflow

> Coming soon

### Chat room

> Coming soon


### FAQ

<details>
<summary>Thread-safe per connection?</summary>

> Currently, the Python driver is not thread-safe. Each thread or multiprocessing PID should be given its own connection object.

</details>


---

### Contact
