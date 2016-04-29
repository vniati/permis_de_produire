
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var io2 = require('socket.io')(http);
var http2 = require('http').Server(app);

var link = require("./function_link.js");

link;

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
});

http.listen(8100, function(){
  console.log('listening on :8100');
});

io.emit('some event');


io2.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io2.emit('chat message', msg);
  });
});

io2.on('connection', function(socket2){
  console.log('a user connected');
  socket2.on('disconnect', function(){
    console.log('user disconnected');
  });
});

http2.listen(8101, function(){
  console.log('listening on :8101');
});

io2.emit('some event');

io2.on('connection', function(socket2){
  socket2.on('chat message2', function(msg2){
    io2.emit('chat message2', msg2);
  });
});
