# important step to create project with enviroment :-

```
// 1) chose your method to create envirement
conda create -p venv  python
py -m venv python
virtualenv env



// 2) create requirements.txt
----flask



// 3) activate your envirements
conda activate path
myword/Scripts/activate
env/Scripts/activate




// 4) pip install -r requirements.txt



// 5) create app.py



// 6) run app.py

```


# Important Notes
```
'debug=True'  :- use for reload page as a new

```




# important command 
```
// check your dependency which install in your environment
pip freeze > requirement.txt


// install dependency using txt file
pip install requirement.txt
```



# Basic syntex of Flask
```
from flask import Flask

app = Flask(__name__)

if __name__=="__main__":
    app.run()

```


# create f() inside
```
@app.route('/')   # this is decoretors
def hello():
    return "<h1>Hellow' World!!</h1>"

```

# Important concept
```
if __name__=='__main__':
    print(__name__)
    app.run(debug=True)

// here '__name__' ko print kiya to output '__main__' agar ussi file par jakar file ko run karte ho. otherwise file na name print ho jayenga. 
```