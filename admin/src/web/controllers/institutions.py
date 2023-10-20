from flask import render_template, flash, redirect, url_for, abort, session
from src.core import institutions
from src.core.auth import find_user_by_email
from flask import Blueprint
from src.web.forms import InstitutionForm, InstitutionSwitchForm
from src.web.helpers.auth import login_required, has_system_permission
from src.web.helpers.maintenance import maintenance_mode_guard


instituciones_bp = Blueprint("institutions", __name__, url_prefix="/consultas_instituciones")

@instituciones_bp.get("/")
@login_required
@maintenance_mode_guard
def institution_index():
    """
    Permite accede al index(listado) del módulo de instituciones
    """
    if not has_system_permission(["institution_index"]):
        return abort(401)

    instituciones = institutions.list_institutions()
    return render_template("instituciones/index.html",instituciones=instituciones)

def institution_show():
    pass


def institution_new():
    pass

@instituciones_bp.route('/create', methods=['GET', 'POST'])
@login_required
@maintenance_mode_guard
def institution_create():
    """
    Permite crear un servicio
    """
    if not has_system_permission(["institution_create"]):
        return abort(401)

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
            flash('La institución se ha creado correctamente.', 'success')
            return redirect(url_for('institutions.institution_index'))
        else:
            flash('Hubo un error al crear la institución.', 'danger')

    return render_template('instituciones/create_institution.html', form=form)


@instituciones_bp.route('/update/<int:institution_id>', methods=['GET', 'POST'])
@login_required
@maintenance_mode_guard
def institution_update(institution_id):
    """
    Permite actualizar una institucion por nombre
    """
    if not has_system_permission(["institution_update"]):
        return abort(401)

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
            flash('La institucion se ha actualizado correctamente.', 'success')
            return redirect(url_for('institutions.institution_index'))
        else:
            flash('Hubo un error al actualizar la institucion.', 'danger')
    else :
        print(form.errors)

    return render_template('instituciones/update_institution.html', form=form, institucion=institucion_actual)



@instituciones_bp.route('/destroy/<int:institution_id>', methods=['GET'])
@login_required
@maintenance_mode_guard
def institution_delete(institution_id):
    """
    Permite eliminar una institucion por nombre
    """
    if not has_system_permission(["institution_destroy"]):
        return abort(401)

    institution_a_eliminar = institutions.get_institution_by_id(institution_id)
    if institution_a_eliminar:
        resultado = institutions.delete_institution(institution_id)
        if resultado:
            flash('El institution se ha eliminado correctamente.', 'success')
        else:
            flash('Hubo un error al eliminar el institution.', 'danger')
    else:
        flash('El institution no se encontró.', 'danger')

    return redirect(url_for('institutions.institution_index'))

@instituciones_bp.route('/switch', methods=['GET', 'POST'])
@login_required
@maintenance_mode_guard
def institution_switch():
    """
    Permite seleccionar otra institución
    """
    user = find_user_by_email(session["user"])

    institutions = []
    for inst in user.institutions:
        institutions.append((
            inst.id,
            inst.name
        ))

    print(institutions)
    form = InstitutionSwitchForm()
    form.institution.choices = institutions

    if form.validate_on_submit():
        print(f"Institution data selected: {form.institution.data}")
        print(form.institution)
        session["institution"] = form.institution.data
        session["institution_name"] = dict(form.institution.choices).get(int(form.institution.data))
        session["institution_count"] = len(user.institutions)
        return redirect(url_for('home'))

    form.institution.data = session["institution"]

    return render_template('instituciones/switch_institution.html', form=form)