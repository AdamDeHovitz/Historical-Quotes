from flask import Flask,render_template, request
import random

app = Flask(__name__)

name = None
quote = None
adjective = None

@app.route("/")
def start():
    return render_template("adamspg.html")

@app.route("/results", methods = ["POST", "GET"])
def main():
    global name
    global quote 
    global adjective
    if name == None:
        name = request.form["name"]
    if quote == None:
        quote = request.form["quote"]
    if adjective == None:
        adjective = request.form["adjective"]
        #print name
   
    s = '''<!doctype html>
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <title>Your page title</title>

        <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
</head>


        <body style="background-color:#E68081">
        '''

    s+= '<h3 class="brand-title"><center><b>Wise words from figures of great stature </b></h3>'

    #s+= "<center>and now for your pleasure a quote: <br><br>"
    get_it = open('quotes.txt', 'r')
    variableName = get_it.read()
    lines= variableName.split('\n')
    lines=lines[:len(lines)-1]
    if quote!='I said nothing':
        lines.append(quote)
        lines.append(quote)
        


    filez = open('namesAndImages.txt', 'r')
    Dict=filez.read()
    Dict=Dict.split('\n')
    Dict=Dict[:len(Dict)-1]
    if name!='I do not know':
        Dict.append(name+',https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ4qlCVQrMo5QqT5-y_pEcycr-HEap5aOoWAHsHtEa3_qJAFxKZA')
        Dict.append(name+',https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ4qlCVQrMo5QqT5-y_pEcycr-HEap5aOoWAHsHtEa3_qJAFxKZA')
    
    Image=Dict[random.randint(0, len(Dict)-1)]
    Image=Image.split(',')

    Name=Image[0]
    image=Image[1]
    filezd = open('Titles.txt', 'r')
    titles=filezd.read()
    titles=titles.split('\n')
    titles=titles[:len(titles)-2]
    if adjective!='indescribable':
        titles.append(adjective)
        titles.append(adjective)
    s+= '<center><img src='+'"'+image+'"'+'width="400" height="400"></img></center><br>'
    s+= '<center>As the '+ titles[random.randint(0, len(titles)-1)]+' <b>'+Name+'</b> once said:<br>'
    s+= '"'+lines[random.randint(0, len(lines)-1)]+'"'
    s+= '''<br><br> 
   <a class="pure-button pure-button-primary" href="/results">A Primary Button</a>
   
'''

    s+= '''<br><br><br> <b> TEST </b> <br> <br>'''
    for allImage in Dict:
        
        allImage=allImage.split(',')

        Name=allImage[0]
        image=allImage[1]
        s+='''<br><br> ''' + Name + "<br><br>"
        s+= '<center><img class="pure-img" src='+'"'+image+'"'+'width="400" height="400"></img></center><br>'
    
    s+= '<br><br><br> <font size="1.5"> <b>*historical accuracy may<br> not be guaranteed'
    filez.close()
    get_it.close()
    filezd.close()



    return s

    
if __name__=="__main__":
    app.debug=True
    app.run()
