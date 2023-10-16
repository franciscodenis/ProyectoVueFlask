from flask import render_template, flash, redirect, url_for
from src.core import institutions
from flask import Blueprint
from src.web.forms import InstitutionForm
from src.web.schemas.institutions import institutions_schema
from flask import request


api_instituciones_bp = Blueprint("institutions_api", __name__, url_prefix="/api/consultas_instituciones")



@api_instituciones_bp.get("/")
def institution_index():
    """
    Permite accede al index(listado) del módulo de instituciones
    """
    list_inst = institutions.list_institutions()
    data = institutions_schema.dumps(list_inst)
    print(type(data))
    return data,200

@api_instituciones_bp.route('/create', methods=['GET', 'POST'])
def institution_create():
    """
    Permite accede al index(listado) del módulo de instituciones
    """
    new_data = request.get_json()
    print("new data: ------>",new_data)
    result = institutions.create_institution(new_data)
    print(result)
    return ({"status": "ok"},201)


    """
    Permite crear un servicio
 
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

        result = institutions.create_institution(new_data)
        
        if result:
            flash('La institución se ha creado correctamente.', 'flash-message-success')
            return redirect(url_for('institutions.institution_index'))
        else:
            flash('Hubo un error al crear la institución.', 'flash-mmesage-error')
    
    return render_template('instituciones/create_institution.html', form=form)
   """
