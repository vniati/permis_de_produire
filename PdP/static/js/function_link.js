var app = require('express')();

app.get('/', function(req, res){
  res.sendfile('/home/virgil/Code/Permis_de_Produire/permis_de_produire/PdP/templates/user.html');
});
