from project import app, db
from flask import render_template, redirect, url_for
from project.finds.forms import AddFind, DelFind
from project.models import Finds


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_find():
    form = AddFind()
    if form.validate_on_submit():
        location = form.location.data
        date = form.date.data
        pic_url = form.pic_url.data
        new_find = Finds(location, date, pic_url)
        db.session.add(new_find)
        db.session.commit()
        return redirect(url_for('thanks'))
    return render_template('add.html', form=form)

@app.route('/del', methods=['GET', 'POST'])
def del_find():
    form = DelFind()
    return render_template('delete.html', form=form)
@app.route('/list')
def finds_list():
    return render_template('list.html')
    # finds = Finds.query.all()
    # return render_template('list.html', finds=finds)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)