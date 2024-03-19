from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/mars')
def mars():
    return """<!doctupe html>
         <html lang="en">
           <head>
             <meta charset="utf-8">
             <title>Отбор астронавтов</title>
             <link rel="stylesheet" href="style1.css">
           </head>
           <body>
              <h1>Анкета претендента на участие в миссии</h1>
               <h3>на участие в миссии</h3>
               <textarea name="NAME"></textarea>
               <br> 
               <textarea name="FAMILIANAME"></textarea><br> 	


               <textarea name="EMAIL"></textarea>
               <p>Какое у вас образование?</p>
               <textarea name="EMAIL"></textarea>
               <p>Какая у вас профессия?</p>
               <input type="radio" name="инженер-исследователь" value="x">
               <p>инженер-исследователь</p>
           </body>
         </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')