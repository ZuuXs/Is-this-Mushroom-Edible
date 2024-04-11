const express = require('express');
const fs = require('fs');
const { spawn } = require('child_process');
const app = express();
app.use(express.static('public'));

// Middlewares to handle form-data
app.use(express.urlencoded({ extended: true }));

app.get('/form', (req, res) => {
    fs.readFile('formulaire.html', 'utf8', (err, data) => {
        if (err) {
            res.status(500).send("Erreur lors du chargement du formulaire");
            return;
        }
        res.send(data);
    });
});


app.post('/rep', (req, res) => {
    // Extraction des données du formulaire
    const R = req.body.R;
    const G = req.body.G;
    const B = req.body.B;
    const shapes = req.body.shape;
    const surfaces = req.body.surface;
    const modele = req.body.modele;
 


    // Choisir le bon fichier de modèle en fonction de l'entrée
    const modelPath = modele === 'svm' ? '../model/svm_model.joblib' : '../model/tree_model.joblib';

    const args = [R, G, B, shapes, surfaces, modelPath];

    
    // Appel du script Python avec les données du formulaire
    const pythonProcess = spawn('python', ['../script/predict.py', ...args]);

    let dataToSend = '';

    pythonProcess.stdout.on('data', (data) => {
        dataToSend += data.toString();
    });


    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            console.error(`Script Python s'est terminé avec le code ${code}`);
            res.status(500).send("Erreur lors de l'exécution du script Python");
            return;
        }
        // Now we send the complete response
        res.send(`Résultat de la prédiction : ${dataToSend}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Erreur : ${data}`);
        res.status(500).send("Erreur lors de l'exécution du script Python");
    });
});

// Démarrer le serveur
const PORT = 8080;
app.listen(PORT, () => { console.log(`Le serveur écoute sur le port ${PORT}`) });