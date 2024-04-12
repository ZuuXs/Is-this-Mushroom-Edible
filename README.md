# Is this Mushroom Edible ?
<p><strong>
The purpose of this project is to learn, by maching learning, to recognize if a mushroom
is edible or poisonous depending on its color, shape and texture of its cuticle.
To do this, we will rely on the site: <br>
  https://ultimate-mushroom.com/.
</strong></p>
<br/>

## Data collecting with python
<p>For the first part, we are going to collect all the data of the website <strong>Ultimate Mushroom</strong> and then save it on a csv file.
  To do so, I created the python file ShroomLearning.py which will go to the main page of the website, parse every link on it, analyse them and collect the data needed for the learning to then save it
 on data/champignons.csv</p>
<br/>

## Data manipulation
<p>In this part, we will convert the CSV data into a format that is compatible with our AI model, facilitating its learning process.
  We'll utilize the <i>'pandas'</i> library in Python to manipulate our data using a DataFrame. Initially, we will configure our DataFrame and perform preliminary 
  calculations to ensure accuracy. Then, we will convert color descriptions into RGB codes and categorize all shapes and surfaces using binary encoding (0 or 1), 
  thus preparing the data for the model's requirements. The script <strong>2ejalon.ipynb</strong> is responsible for performing these operations </p>
<br/>

## Learning and shaping
<p>Finally, we will commence the training process using the scikit-learn library. We will experiment with two types of models: <strong>Support Vector Machine (SVM)</strong> and <strong>Decision Tree</strong>.
  For each model, we will conduct training sessions both with and without a scaler to compare prediction differences using accuracy scores and confusion matrices.
  This approach will help us understand the importance of avoiding overfitting in our models.The same file mentioned earlier, <strong>2ejalon.ipynb</strong>, is responsible for this learning process. 
  After completing the training, we will use the <i>'joblib'</i> library to save our trained models for future use. </p>
<br/>

## Launching and testing the APP
<p>We begin by setting up a <strong>Node.js Express framework</strong> and create a straightforward webpage using HTML <strong>formulaire.html</strong>.
  We then utilize <strong>the index.js</strong> file to handle server requests and implement the <strong>script/predict.py</strong> code to generate predictions using one of the two models.</p>
<br/>

## How to try the project
<ol>
  <li>Clone or Download zip file from the git repository.</li>
  <li>Install node.js in your device</li>
  <li>Launch a CMD inside the directory of the ProjetExpress</li>
  <li>To launch the local server type : "node index.js"</li>
  <li>Go to your favorite browser and enter this link : http://localhost:8080/form</li>
  <li>Fill the informations of the mushroom you want to test</li>
  <li>Submit, enjoy the result</li>
</ol>
<strong>It is important to note that the results may not always be accurate, as the AI model used in this process is relatively basic.</strong>
