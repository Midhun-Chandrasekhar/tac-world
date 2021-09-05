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

<h2>Project Architecture</h2>
<ul>
<li>1 Load Balancer(Nginx) - Act as the primary contact node to public</li>
<li>Entire App including the index page will be serverd by Gunicorn + eventlet workers</li>
<li>2 App server is deployed to support the platform to provide better performance</li>
<li>Every request to the Load balancer is proxied to App servers</li>
<li>1 Redis server is used as Message queue. This can help the App servers to coordinate each other</li>
<li>Redis support the system from failure tolerence.</li>
<li>1 MongoDB is used as the central Database to store information related to User and Messages</li>
<li>MongoEngine is used as ODM and DB manager</li>
<li>Architecture diagram with 4 App server is attached in docs/documents/</li>
<li>Application Document is attached in docs/documents/</li>
</ul>

<h2>Project Setup</h2>
<h4>Container Local deployment</h4>
<ul>
<li>Setup Docker</li>
<li>Enter the Main Directory</li>
<li>Execute: docker-compose up --build --scale app=2</li>
<li>Entire Stack with Loadbalance, 2 App server, 1 Redis server and 1 MongoDB will start</li>
<li>Visit url: http://localhost:81/</li>
<li>Load Testing: python tac/test/test_chat.py (Note: Install requirements.txt)</li>
</ul>

<h2>Result</h2>
<li>Load Test on 50+ Virtual concurrent client on single flask worker</li>
<li>Load Test on 100+ Virtual concurrent client on single App server</li>
<li>Load Test on 510+ Virtual concurrent client on 1 LoadBalancer + 2 App Server + 1 DB + 1 Message Queue</li>
<li>Screenshots of the results are attached in docs/load-test-results/</li>
</ul>

<h2>Future Scope</h2>
<li>FE migration to React</li>
<li>User Enhancemnet</li>
<li>Multiroom support</li>
<li>Multimedia messaging</li>
<li>Real time Audio/Video conference</li>
<li>FE Mobile Application using ReactNative</li>
<li>AI</li>
</ul>