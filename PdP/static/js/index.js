var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendfile('/home/virgil/Code/Permis_de_Produire/permis_de_produire/PdP/templates/user.html');
});

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
});

http.listen(8100, function(){
  console.log('listening on :8100');
});



io.emit('some event', { for: 'everyone' });

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});
