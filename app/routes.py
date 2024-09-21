from flask import Blueprint, render_template, request, redirect, url_for
from . import db
import re
from .models import Inventory

main = Blueprint('main', __name__)

@main.route('/')
def index():
    items = Inventory.query.all()
    return render_template('index.html', items=items)

@main.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        mac_address = request.form.get('mac_address')
        serial_number = request.form.get('serial_number')
        manufacturer = request.form.get('manufacturer')
        description = request.form.get('description')

        errors = []

        if not name or not price or not mac_address or not serial_number or not manufacturer or not description:
            errors.append('All fields are required.')

        if len(mac_address) > 17 or not re.match(r'([0-9A-Fa-f]{2}[:-]?){5}[0-9A-Fa-f]{2}', mac_address):
            errors.append('MAC Address must be valid and follow the format (e.g., 00:0a:95:9d:68:16).')

        if errors:
            return render_template('add_item.html', errors=errors, form_data=request.form)

        try:
            new_item = Inventory(
                name=name,
                price=float(price),
                mac_address=mac_address,
                serial_number=serial_number,
                manufacturer=manufacturer,
                description=description
            )
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            errors.append(f"Error adding item to database: {str(e)}")
            return render_template('add_item.html', errors=errors, form_data=request.form)

    return render_template('add_item.html')


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    item = Inventory.query.get(id)
    if request.method == 'POST':
        item.name = request.form.get('name')
        item.price = float(request.form.get('price'))
        item.mac_address = request.form.get('mac_address')
        item.serial_number = request.form.get('serial_number')
        item.manufacturer = request.form.get('manufacturer')
        item.description = request.form.get('description')

        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_item.html', item=item)


@main.route('/delete/<int:id>')
def delete_item(id):
    item = Inventory.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/db_test')
def db_test():
    try:
        db.session.execute('SELECT 1')
        return 'Database Connected Successfully'
    except Exception as e:
        return f'Database Connection Failed: {e}'
