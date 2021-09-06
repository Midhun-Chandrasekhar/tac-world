const chat = document.getElementById('chat');
const inp_message = document.getElementById('inp_message');
const send = document.getElementById('send');
const username = document.getElementById('username');
const btn_connect = document.getElementById('connect');
const btn_disconnect = document.getElementById('disconnect');
const btn_info = document.getElementById('info');
const back = document.getElementById('back');
const roomView = document.getElementById('room');
const logView = document.getElementById('login');
const userListView = document.getElementById('userlist');
const userBox = document.getElementById('user-box');
const loader = document.getElementById('loader');

const windowSize = 100;
let socket;
const endPoint = "http://localhost:81/";


const headerOptions = (user) => {
  return {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    user
  }
};


const buildUserTile = (user_name) => {
  const card = document.createElement('div');
  const pic = document.createElement('div');
  const name = document.createElement('p');

  card.className = 'user-tile';
  pic.className = "dot";

  pic.innerHTML = user_name[0];
  name.innerText = user_name;

  card.appendChild(pic);
  card.appendChild(name);
  return card;
};


const buildUserTiles = (users) => {
  let child;
  for (let key in users) {
    child = buildUserTile(users[key]);
    userBox.append(child);
  };
};

const buildMessage = (data) => {
  const card = document.createElement('div');
  const pic = document.createElement('div');
  const msg = document.createElement('div');
  const txt = document.createElement('p');
  const time = document.createElement('p');
  const user = document.createElement('p');

  pic.className = "dot";
  msg.className = "msg-card";
  user.className = "name";
  time.className = "time";
  txt.className = "msg";

  pic.innerHTML = data.sender[0];
  txt.innerHTML = data.text;
  time.innerHTML = "Time : " + data.created_at;
  
  if (data.sender === username.value){
    card.className = "message-box-right";
    msg.appendChild(txt);
    msg.appendChild(time);
    card.appendChild(msg);
    card.appendChild(pic);
  }
  else{
    user.innerHTML = data.sender;
    card.className = "message-box-left";
    msg.appendChild(user);
    msg.appendChild(txt);
    msg.appendChild(time);
    card.appendChild(pic);
    card.appendChild(msg);
  }
  return card;
}

const injectChats = (messages) => {
  let child;
  for (let key in messages) {
    child = buildMessage(messages[key]);
    if (chat.childElementCount > windowSize) chat.removeChild(chat.childNodes[0]);
    chat.appendChild(child);
    chat.scrollTop = chat.scrollHeight - chat.clientHeight;
  };
}

const switchView = (view) => {
  switch(view) {
    case "loader":
      loader.style.display = "block";
      userListView.style.display = "none";
      roomView.style.display = "none";
      logView.style.display = "none";

      break;
    case "userlist":
      userListView.style.display = "flex";
      roomView.style.display = "none";
      logView.style.display = "none";
      loader.style.display = "none";
      break;
    case "chat":
      userListView.style.display = "none";
      roomView.style.display = "flex";
      logView.style.display = "none";
      loader.style.display = "none";
      break;
    default:
      logView.style.display = "flex";
      userListView.style.display = "none";
      roomView.style.display = "none";
      loader.style.display = "none";
  };
};


const doLogin = async (user_name) => {
  switchView("loader");
  try{
    const rawResponse = await fetch(endPoint+'users/login', {
      method: 'POST',
      headers: headerOptions(),
      body: JSON.stringify({user_name})
    });
    const response = await rawResponse.json();
    if (response.status === "ok" && response.message === "login_success" || response.message === "acc_created"){
      const options = {autoConnect: false, extraHeaders: {user:username.value}, cors: { origin: "*"}};
      socket = io(options);
      socket = exe_sock(socket);
      socket.connect();
      getChats();  
    }
    else{
      console.log("unexpected respose", response);
      // TODO: Toast message or neccesary action
    };
  }
  catch(e){
    console.log("Something went wrong", e);
    // TODO: Toast message or neccesary action
  }
};


const getUsers = async () => {
  switchView("loader");
  try{
    const rawResponse = await fetch(endPoint+'users/', {
      headers: headerOptions(username.value)
    });
    const response = await rawResponse.json();
    if (response.status === "ok" && response.message === "user_list"){
      switchView("userlist");
      buildUserTiles(response.data);
    }
    else console.log("unexpected respose");
    // TODO: Toast message or neccesary action
  }
  catch(e){ 
    console.log("Something went wrong", e);
    // TODO: Toast message or neccesary action
  }
};


const getChats = async () => {
  switchView("loader");
  try{
    const rawResponse = await fetch(endPoint+'chats/', {
      headers: headerOptions(username.value)
    });
    const response = await rawResponse.json();
    if (response.status === "ok" && response.message === "chat_history"){
      injectChats(response.data);
      switchView("chat");
    }
    else console.log("unexpected respose", response);
    // TODO: Toast message or neccesary action
  }
  catch(e){
    console.log("Something went wrong", e);
    // TODO: Toast message or neccesary action
  }
};




btn_connect.onclick = ()=>{
    if(username.value != "") {
      doLogin(username.value);
    }
    else {
        alert("Please enter an username!");
    }
};


btn_info.onclick = ()=> getUsers();

back.onclick = () => switchView("chat");

btn_disconnect.onclick = () => {
  socket.close();
  switchView();
};

send.onclick = () => {
  socket.emit('message', {text:inp_message.value});
  inp_message.value = "";
};

const exe_sock = (socket) => {
socket.on('connect', () => console.log("Connected to server!"));

socket.on('disconnect', function(){
    console.log('Disconnected to server!')
    socket.close();
    switchView();
});

socket.on('notify', function(data){
  if (!data) return;
  data = JSON.parse(data).message;
  if (chat.childElementCount > windowSize) chat.removeChild(chat.childNodes[0]);
  chat.appendChild(buildMessage(data));
  chat.scrollTop = chat.scrollHeight - chat.clientHeight;
});
return socket;
}
