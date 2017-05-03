from flask import Flask, render_template, request
from flask_migrate import Migrate
from model import db, Appartment
from config import POST_PER_PAGE, SECRET_KEY
from datetime import datetime
from sqlalchemy import func

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.config.from_object('config')
app.secret_key = SECRET_KEY
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def filter():
    current_page = request.args.get('page', 1)
    args = dict(request.args)
    args.pop('page',None)
    maximum_price = db.session.query(func.max(Appartment.price)).one()[0]

    ads = Appartment.query.filter(
        '' if not request.args.get('new_building') else Appartment.construction_year >= (datetime.now().year - 2),
        Appartment.price < request.args.get('max_price', maximum_price, type=int),
        Appartment.price > request.args.get('min_price', 0, type=int),
        Appartment.oblast_district == request.args.get('oblast_district'),
        Appartment.active.is_(True)).paginate(int(current_page), POST_PER_PAGE)

    return render_template('ads_list.html', args=args, ads=ads)


if __name__ == "__main__":
    app.run()
