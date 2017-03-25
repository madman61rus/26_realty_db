from flask import Flask, render_template, request, session
from flask_migrate import Migrate
from model import db, Appartment
from config import POST_PER_PAGE, SECRET_KEY
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = SECRET_KEY
db.init_app(app)
migrate = Migrate(app, db)


def request_oblast_district():
    if request.args.get('oblast_district'):
        return ' oblast_district = "{}" '.format(request.args.get('oblast_district'))
    else:
        return ''


def request_new_building():
    now = datetime.now().year
    if request.args.get('new_building'):
        return ' AND ( under_construction = {} OR ({} - construction_year) < 2 ) '.format(
            1 if session['new_building'] else 0, now)
    else:
        return ''


def request_max_price():
    if request.args.get('max_price'):
        return ' AND price <= {} '.format(request.args.get('max_price'))
    else:
        return ''


def request_min_price():
    if request.args.get('min_price'):
        return ' AND price >= {} '.format(request.args.get('min_price'))
    else:
        return ''


def make_query():
    return request_oblast_district()  + \
           request_new_building()  + \
           request_max_price()  + \
           request_min_price()


@app.route('/')
def filter():
    current_page = request.args.get('current_page') or '1'
    print(make_query())

    ads = Appartment.query.filter(make_query()).paginate(int(current_page), POST_PER_PAGE)

    return render_template('ads_list.html',
                           args=request.args,
                           ads=ads)


if __name__ == "__main__":
    app.run()
