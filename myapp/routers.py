from hashids import Hashids
from flask import (
    render_template, 
    request, 
    flash, 
    redirect, 
    url_for,
    Blueprint
)
from .models import ShortUrl
from .extentions import db


main = Blueprint('main', __name__)

hashids = Hashids(min_length=4, salt='somestring')


@main.route('/', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))

        url_data = ShortUrl(original_url=url)

        db.session.add(url_data)
        db.session.commit()

        hashid = hashids.encode(url_data.id)
        short_url = request.host_url + hashid

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


@main.route('/<url_id>')
def url_redirect(url_id):

    original_id = hashids.decode(url_id)
    if original_id:
        original_id = original_id[0]

        if len(ShortUrl.query.all()) >= 20:
            flash('Too many URLs in the database')
            return redirect(url_for('index'))    
        
        data = ShortUrl.query.get(original_id)

        return redirect(data.__dict__['original_url'])
    
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))
    