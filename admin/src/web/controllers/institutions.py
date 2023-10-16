from flask import render_template, flash, redirect, url_for
from src.core import institutions
from flask import Blueprint
from src.web.forms import InstitutionForm


instituciones_bp = Blueprint("institutions", __name__, url_prefix="/consultas_instituciones")

@instituciones_bp.get("/")
def institution_index():
    """
    Permite accede al index(listado) del módulo de instituciones
    """
    instituciones = institutions.list_institutions()
    return render_template("instituciones/index.html",instituciones=instituciones)

def institution_show():
    pass


def institution_new():
    pass

@instituciones_bp.route('/create', methods=['GET', 'POST'])
def institution_create():
    """
    Permite crear un servicio
    """
    form = InstitutionForm()
    if form.validate_on_submit():
        # Procesa los datos del formulario y crea la institucion en la base de datos
        new_data = {
            'name':form.name.data,
            'address':form.address.data,
            'information':form.information.data,
            'location':form.location.data,
            'web':form.web.data,
            'keywords':form.keywords.data,
            'opening_hours':form.opening_hours.data,
            'contact':form.contact.data,
            'has_authorization':form.has_authorization.data
        }

        result = institutions.create_institution(**new_data)
        
        if result:
            flash('La institución se ha creado correctamente.', 'flash-message-success')
            return redirect(url_for('institutions.institution_index'))
        else:
            flash('Hubo un error al crear la institución.', 'flash-mmesage-error')
    
    return render_template('instituciones/create_institution.html', form=form)


@instituciones_bp.route('/update/<int:institution_id>', methods=['GET', 'POST'])
def institution_update(institution_id):
    """
    Permite actualizar una institucion por nombre
    """
    institucion_actual = institutions.get_institution_by_id(institution_id)
    form = InstitutionForm(obj=institucion_actual)
    
    if form.validate_on_submit():
        
        # Procesa los datos del formulario y actualiza el servicio en la base de datos
        new_data = {
            'name':form.name.data,
            'address':form.address.data,
            'information':form.information.data,
            'location':form.location.data,
            'web':form.web.data,
            'keywords':form.keywords.data,
            'opening_hours':form.opening_hours.data,
            'contact':form.contact.data,
            'has_authorization':form.has_authorization.data
        }

        print(new_data)

        result = institutions.update_institution(institution_id, new_data)
        
        if result:
            flash('La institucion se ha actualizado correctamente.', 'flash-message-success')
            return redirect(url_for('institutions.institution_index'))
        else:
            flash('Hubo un error al actualizar la institucion.', 'flash-mmesage-error')
    else :
        print(form.errors)
    
    return render_template('instituciones/update_institution.html', form=form, institucion=institucion_actual)



@instituciones_bp.route('/destroy/<int:institution_id>', methods=['GET'])
def institution_delete(institution_id):
    """
    Permite eliminar una institucion por nombre
    """
    institution_a_eliminar = institutions.get_institution_by_id(institution_id)
    if institution_a_eliminar:
        resultado = institutions.delete_institution(institution_id)
        if resultado:
            flash('El institution se ha eliminado correctamente.', 'flash-message-success')
        else:
            flash('Hubo un error al eliminar el institution.', 'flash-mmesage-error')
    else:
        flash('El institution no se encontró.', 'flash-mmesage-error')
    
    return redirect(url_for('institutions.institution_index'))