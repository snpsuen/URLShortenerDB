from flask import Flask, render_template, request, redirect, url_for
import pymongo, pickle, random, string
import os.path

def randomstring(length):
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length
        )
    )

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/shortenurl', methods=['GET', 'POST'])
def shortenurl():
    if request.method == 'POST':
      absolute = request.form['url']
      shorten = randomstring(8)
      
      democlient = pymongo.MongoClient("mongodb://mongodemo:mongodemo@mongodemo-service:27017")
      demodb = democlient['demo']
      democollect = demodb['urlmap']
      
      newdict['shorturl'] = shorten
      newdict['fullurl'] = absolute
      x = democollect.insert_one(newdict)
      democlient.close()  
    
      return render_template('result.html', variable=shorten)
    
@app.route('/<shortpath>')
def travel(shortpath):
    democlient = pymongo.MongoClient("mongodb://mongodemo:mongodemo@mongodemo-service:27017")
    demodb = democlient['demo']
    democollect = demodb['urlmap']
    
    query['shorturl'] = shortpath
    found = democollect.find_one(query)
    democlient.close()
    
    if found != None:
        absolute = found['fullurl']
        return redirect(absolute)
    else:
        return(f"Short URL ({shortpath}) is not found!\n")
