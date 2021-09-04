<h1>Tac World</h1>
<p>Real Time scalable chat application</p>
<br>
<p><b>Auther: </b> Midhun Chandrasekhar</p>
<p><b>Software Architect / Engineer</b></p>
<p><b>Contact : </b>csekhar.jr@gmail.com</p>
<br>
<h2>Over View</h2>
<p>
Real Time Chat application based on sockets. The application primarily focus
on conducting group chat for Engineer, Developers and other technology enthusiast.
Application is a bare minimal implementation using the client server architecture 
as the backbone of the system.
</p>
<p>
The Application server plays a vital role is providing the REST API, TCP Sockets 
and also act as the FE server.
</p>

<h2>Stack</h2>
<h4>Front End</h4>
<ul>
<li>HTML</li>
<li>Javascript</li>
<li>Jquery</li>
<li>Bootstrap4</li>
<li>Socketio</li>
</ul>
<br>
<h4>Back End</h4>
<ul>
<li>Python 3.8</li>
<li>Flask</li>
<li>Flask-socketio</li>
<li>MongoDB</li>
<li>MongoEngine</li>
<li>Redis</li>
<li>Gunicorn</li>
<li>Eventlet</li>
<li>Socketio</li>
<li>Docker</li>
</ul>

<h2>Project Setup</h2>
<h4>Bare Metal deployment</h4>
<ul>
<li>Setup MongoDB</li>
<li>Setup Redis Server</li>
<li>Setup Python 3.8 Virtual Environment</li>
<li>Install the requirements using "pip install -r requirements.txt"</li>
<li>Update the configurations in the settings directory</li>
<li>run app using: gunicorn --worker-class eventlet dev_server:app</li>
<li>Visit url: http://localhost:8000/ (check conf for modification)</li>
<li>Load Testing: python test/test_chat.py (update the settings)</li>
</ul>

<h2>Result</h2>
<p>Load Test on 55 Virtual concurrent client on single Worker deployment</p>
![alt text](https://github.com/Midhun-Chandrasekhar/tac-world/tree/main/tac/docs/images/loadt.png?raw=true)