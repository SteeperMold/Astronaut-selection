import os
from flask import Flask, url_for, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/media')


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lines = (
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    )

    return "<br>".join(lines)


@app.route('/image_mars')
def image_mars():
    return f"<b>Жди нас, Марс!</b><br>" \
           f"<img src={url_for('static', filename='img/MARS.png')}>" \
           f"<p>Вот она какая, красная планета</p>"


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                     <link rel="stylesheet"
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                     crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                    <title>Пример загрузки файла</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1><br>
                    <img src={url_for('static', filename='img/MARS.png')}>
                    <p class="alert alert-secondary">Человечество вырастает из детства.</p>
                    <p class="alert alert-success">Человечеству мала одна планета.</p>
                    <p class="alert alert-dark">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="alert alert-warning">И начнем с Марса!</p>
                    <p class="alert alert-danger">Присоединяйся!</p>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=["GET", "POST"])
def astronaut_selection():
    if request.method == "GET":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                      </head>
                      <body>
                        <h1>Анкета претендента</h1>
                        <h2>на участие в миссии</h2>
                        <form class="login_form" method="post">
                            <div class="form-group">
                                <input class="form-control" name="surname" placeholder="Введите фамилию">
                                <input class="form-control" name="name" placeholder="Введите имя">
                                <br>
                                <input class="form-control" type="email" name="email" placeholder="Введите адрес почты">
                            </div>
                            <div class="form-group">
                            <label for="education-select">Какое у Вас образование?</label>
                                <select class="form-control" id="education-select" name="education">
                                  <option>Начальное</option>
                                  <option>Основное общее</option>
                                  <option>Среднее общее</option>
                                  <option>Высшее</option>
                                </select>
                             </div>
                            <div class="form-group">
                                <label for="job" class="form-check-label">Какие у Вас есть профессии?</label>
                                <div class="form-check">
                                    <input name="job" id="research-engineer" class="form-check-input" type="radio" value="research-engineer">
                                    <label class="form-check-label" for="job">Инженер-исследователь</label>
                                </div>
                                <div class="form-check">
                                    <input name="job" id="pilot" class="form-check-input" type="radio" value="pilot">
                                    <label class="form-check-label" for="pilot">Пилот</label>
                                </div>
                                <div class="form-check">
                                    <input name="job" id="builder" class="form-check-input" type="radio" value="builder">
                                    <label class="form-check-label" for="builder">Строитель</label>
                                </div>
                                <div class="form-check">
                                    <input name="job" id="exobiologist" class="form-check-input" type="radio" value="exobiologist">
                                    <label class="form-check-label" for="exobiologist">Экзобиолог</label>
                                </div>
                                <div class="form-check">
                                    <input name="job" id="doctor" class="form-check-input" type="radio" value="doctor">
                                    <label class="form-check-label" for="doctor">Врач</label>
                                </div>
                                <div class="form-check">
                                    <input name="job" id="terraforming-engineer" class="form-check-input" type="radio" value="terraforming-engineer">
                                    <label class="form-check-label" for="terraforming-engineer">Инженер по терраформированию</label>
                                </div>
                                <div class="form-check">
                                    <input name="job" id="climatologist" class="form-check-input" type="radio" value="climatologist">
                                    <label class="form-check-label" for="climatologist">Климатолог</label>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="form-check">Укажите пол</label>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                  <label class="form-check-label" for="male">
                                    Мужской
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                  <label class="form-check-label" for="female">
                                    Женский
                                  </label>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="textarea">Почему Вы хотите принять участие в миссии?</label>
                                <textarea class="form-control" id="textarea" name="motivation"></textarea>
                            </div>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="checkbox" name="accept">
                                <label class="form-check-label" for="checkbox" name="accept">Готовы остаться на Марсе?</label>
                            </div>
                            <button type="submit" class="btn btn-primary">Записаться</button>
                        </form>
                      </body>
                    </html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                     <link rel="stylesheet"
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                     crossorigin="anonymous">
                    <title>Пример загрузки файла</title>
                  </head>
                <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <p class="alert alert-secondary">Эта планета близка к Земле;</p>
                    <p class="alert alert-success">На ней много необходимых ресурсов;</p>
                    <p class="alert alert-dark">На ней есть вода и атмосфера;</p>
                    <p class="alert alert-warning">На ней есть большое магнитное поле;</p>
                    <p class="alert alert-danger">Наконец, она просто красива!</p>
                </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                     <link rel="stylesheet"
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                     crossorigin="anonymous">
                    <title>Пример загрузки файла</title>
                  </head>
                <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в мииссии {nickname}:</h2>
                    <p class="alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора:</p>
                    <p>составляет {rating}!</p>
                    <p class="alert-warning">Желаем удачи!</p>
                </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                         <link rel="stylesheet"
                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                         crossorigin="anonymous">
                        <title>Пример загрузки файла</title>
                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" 
                        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" 
                        crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" 
                        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" 
                        crossorigin="anonymous"></script>
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" 
                        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" 
                        crossorigin="anonymous"></script>
                      </head>
                    <body>
                        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                            <ol class="carousel-indicators">
                                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                            </ol>
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img class="d-block w-100" src="/static/img/3.jpg" alt="First slide">
                                </div>
                                <div class="carousel-item">
                                    <img class="d-block w-100" src="/static/img/2.jpg" alt="Second slide">
                                </div>
                                <div class="carousel-item">
                                    <img class="d-block w-100" src="/static/img/1.jpg" alt="Third slide">
                                </div>
                            </div>
                            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                            </a>
                            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                            </a>
                        </div>
                    </body>
                    </html>"""


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    photo = ''

    if request.method == 'POST':
        file = request.files['photo']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo = f"""<img src="{url_for('static', filename='media/' + filename)}" class="img-fluid">"""

    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                         <link rel="stylesheet"
                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                         crossorigin="anonymous">
                        <title>Пример загрузки файла</title>
                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" 
                        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" 
                        crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" 
                        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" 
                        crossorigin="anonymous"></script>
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" 
                        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" 
                        crossorigin="anonymous"></script>
                      </head>
                    <body>
                    
                        <form method="POST" action="" enctype="multipart/form-data">
                        <div class="form-group">
                            <input type="file" name="photo" class="form-control-file">
                        </div>
                        {photo}
                        <button type="submit" class="btn btn-primary">Upload</button>
                    </form>
                    
                    </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
