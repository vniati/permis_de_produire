var app = require('express')(),
server = require('http').createServer(app),
io = require('socket.io').listen(server),
ent = require('ent'), // Permet de bloquer les caractères HTML (sécurité équivalente à htmlentities en PHP)
fs = require('fs');


// Chargement de la page index.html
app.get('/', function (req, res) {
 res.sendfile(__dirname + '/user.html');
});

io.sockets.on('connection', function (socket, pseudo) {
   // Dès qu'on nous donne un pseudo, on le stocke en variable de session et on informe les autres personnes
   socket.on('nouveau_client', function(pseudo) {
       pseudo = ent.encode(pseudo);
       socket.pseudo = pseudo;
       socket.broadcast.emit('nouveau_client', pseudo);
   });

   // Dès qu'on reçoit un message, on récupère le pseudo de son auteur et on le transmet aux autres personnes
   socket.on('message', function (message) {
       message = ent.encode(message);
       socket.broadcast.emit('message', {pseudo: socket.pseudo, message: message});
       //socket.broadcast.emit('message', message);
   });
});

server.listen(8081);
/*
var app_reponse = require('express')(),
server_reponse = require('http').createServer(app_reponse),
io_reponse = require('socket.io').listen(server_reponse),
ent_reponse = require('ent'), // Permet de bloquer les caractères HTML (sécurité équivalente à htmlentities en PHP)
fs_reponse = require('fs');
/*
// Chargement de la page index.html
app_reponse.get('/', function (req, res) {
 res.sendfile(__dirname + '/user.html');
});*/

io.sockets.on('connection', function (socket, pseudo) {
   // Dès qu'on nous donne un pseudo, on le stocke en variable de session et on informe les autres personnes
   socket.on('nouveau_client_reponse', function(pseudo) {
       pseudo = ent.encode(pseudo);
       socket.pseudo = pseudo;
       socket.broadcast.emit('nouveau_client_reponse', pseudo);
   });

   // Dès qu'on reçoit un message, on récupère le pseudo de son auteur et on le transmet aux autres personnes
   socket.on('message_reponse', function (message) {
       message = ent.encode(message);
       socket.broadcast.emit('message_reponse', {pseudo: socket.pseudo, message: message});
   });
});

server.listen(8081);
