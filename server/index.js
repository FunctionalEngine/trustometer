// const serviceRouter = require('./api/services');
const express = require('express');
const app = express();
const cors = require('cors');
const fs = require('fs');

const rawdata = fs.readFileSync('env.cred.json');  
const credentials = JSON.parse(rawdata);  


//middlewares
app.use(express.json());
app.use(cors());

app.post('/', (req, res) => {
    getTrustScore(req.body.url, credentials.AWS_USER, credentials.AWS_CREDENTIALS)
    .then(function(getTrustScore) {
        res.send(getTrustScore.toString());
    })
    .catch(function(getTrustScore) {
        console.log(getTrustScore.toString());
    });
})

const getTrustScore = function ( url, user, credentials){
    
    return new Promise(function(success, nosuccess) {

        const { spawn } = require('child_process');
        const pyprog = spawn('python3', ['./api/python/score.py', url, user, credentials]);

        pyprog.stdout.on('data', function (data) {
            success(data);
        });

        pyprog.stderr.on('data', (data) => {
            nosuccess(data);
        });
    });
}


app.listen(5000, (err) => {
    console.log('Servidor listo en el puerto ' + 5000);
})