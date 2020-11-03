from project import app, db
from flask import render_template, redirect, url_for,request
from project.finds.forms import AddFind, DelFind
from project.models import Finds, Snakes



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_find():
    form = AddFind()
    if form.validate_on_submit():
        species_id = form.species_id.data
        location = form.location.data
        date = form.date.data
        pic = request.files['pic'].read()
        new_find = Finds(species_id, location, date, pic)
        db.session.add(new_find)
        db.session.commit()
        return redirect(url_for('thanks'))
    return render_template('add.html', form=form)


@app.route('/findslist')
def finds_list():
    finds = Finds.query.all()
    return render_template('finds_list.html', finds=finds)
@app.route('/snakelist')
def snake_list():
    snakes = Snakes.query.all()
    return render_template('snake_list.html', snakes=snakes)

@app.route('/species/<id>')
def species_id(id):
    snakes = Snakes.query.all()
    finds = Finds.query.filter_by(species_id=id)
    return render_template('species_id.html', finds=finds, snakes=snakes)












@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/viperidae')
def viperidae():
    return render_template('viperidae.html')

@app.route('/colubridae')
def colubridae():
    return render_template('colubridae.html')

@app.route('/typhlopidae')
def typhlopidae():
    return render_template('typhlopidae.html')

@app.route('/boidae')
def boidae():
    return render_template('boidae.html')

if __name__ == '__main__':
    #
    # data = [('Xerotyphlops vermicularis', 'გველბრუცა'),
    #         ('Eryx jaculus', 'დასავლეთის მახრჩობელა'),
    #         ('Coronella austriaca', 'სპილენძა'),
    #         ('Dolichophis schmidti', 'წითელმუცელა მცურავი'),
    #         ('Eirenis collaris', 'საყელოიანი ეირენისი'),
    #         ('Eirenis modestus', 'წყნარი ეირენისი'),
    #         ('Elaphe dione', 'სახეებიანი მცურავი'),
    #         ('Elaphe urartica', 'ურარტუს ოთხზოლიანი მცურავი'),
    #         ('Hemorrhois ravergieri', 'ნაირფერი მცურავი'),
    #         ('Molpolon insignitus', ' აღმოსავლური ხვლიკიჭამია გველი'),
    #         ('Natrix natrix', 'ჩვეულებრივი ანკარა'),
    #         ('Natrix tessellata', 'წყლის ანკარა'),
    #         ('Platyceps najadum', 'წენგოსფეწრი მცურავი'),
    #         ('Telescopus fallax', 'კატისთვალა გველი'),
    #         ('Zamenis hohenackeri', 'ამიერკავკასიური მცურავი'),
    #         ('Zamenis longissimus', 'ესკულაპის მცურავი'),
    #         ('Macrovipera lebetina', 'გიურზა'),
    #         ('Vipera transcaucasiana', 'ამიერკავკასიური ცხვირრქოსანი გველგესლა'),
    #         ('Vipera darevskii', 'დარევსკის გველგესლა'),
    #         ('Vipera dinniki', 'დინიკის გველგესლა'),
    #         ('Vipera eriwanensis', 'სომხური ველის გველგესლა'),
    #         ('Vipera kaznakovi', 'კავკასიური გველგესლა')
    #         ]
    #
    # for item in data:
    #     snake = Snakes(item[0], item[1])
    #     db.session.add(snake)
    #
    # db.session.commit()
    app.run(debug=True, port=8000)
