var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var link = require('./function_link.js');

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
