def list_instituciones():
    instituciones = [
        {"nombre": "institucion1",
         "informacion": "informacion institución 1",
         "direccion": "dirección institución 1",
         "localizacion": "localización institución 1",
         "web": "www.webinstitucion1.com",
         "palabras_clave" :["uno","1","primero"],
         "dias_horarios_atencion" : "Lun a Vier de 7 a 19",
         "contacto":"institución1@hotmail.com",
         "habilitado":True},
        {"nombre": "institucion2",
         "informacion": "informacion institución 2",
         "direccion": "dirección institución 2",
         "localizacion": "localización institución 2",
         "web": "www.webinstitucion1.com",
         "palabras_clave" :["dos ","2","segundo"],
         "dias_horarios_atencion" : "Lun a Vier de 7 a 19",
         "contacto":"institución2@hotmail.com",
         "habilitado":False}
         
    ]
    return instituciones