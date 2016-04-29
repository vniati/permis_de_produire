var app = require('express')();


app.get('/', function(req, res){
  res.sendfile('/home/lbarthes/Code/Permis_de_produire_env/permis_de_produire/PdP/templates/user.html');
});
