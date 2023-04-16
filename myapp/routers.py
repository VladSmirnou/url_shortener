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
import uuid


main = Blueprint('main', __name__)

hashids = Hashids(min_length=4, salt=str(uuid.uuid4))

@main.route('/', methods=('GET',))
def home_page():
    return render_template('home_page.html')


@main.route('/url_list')
def display_url_list():
    urls = ShortUrl.query.all()
    return render_template('url_list.html', urls=urls)


@main.route('/shorturl', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('The URL is required!')
            return redirect(url_for('main.index'))

        if res:= len(ShortUrl.query.all()) >= 20:
            flash('Too many URLs in the database')
            return redirect(url_for('main.index'))

        url_data = ShortUrl(id=res + 1, original_url=url)

        hashid = hashids.encode(url_data.id)
        short_url = request.host_url + hashid

        url_data.short_url = short_url

        db.session.add(url_data)
        db.session.commit()
        flash(f'URL {url_data.original_url} was added to the database')
        return redirect(url_for('main.home_page'))

    return render_template('url_form.html')


@main.route('/<url_id>')
def url_redirect(url_id):

    original_id = hashids.decode(url_id)
    if original_id:
        original_id = original_id[0]  
        
        data = ShortUrl.query.get(original_id)

        return redirect(data.__dict__['original_url'])
    
    else:
        flash('Invalid URL')
        return redirect(url_for('main.home_page'))
    