def diagSintoma(var_pat) :
    diccionario = {
        'id_diagnostico' : var_pat['id_diagnostico'],
        'resultado': 'enfermedad',
        'estado': 'id_estado'
        }
    if var_pat['diag_ta'] == 'Si' and var_pat['diag_pa'] == 'Si'and var_pat['diag_do'] == 'Si' and var_pat['diag_dg'] =='Si':
        diccionario=diccionario.copy()
        diccionario['resultado']='Dengue'
        diccionario['estado']= True
    elif var_pat['diag_ta'] == 'Si' and var_pat['diag_pa'] == 'No'and var_pat['diag_do'] == 'No' and var_pat['diag_dg'] =='Si':
        diccionario=diccionario.copy()
        diccionario['resultado']='Gripa'
        diccionario['estado']= True
    elif var_pat['diag_ta'] == 'No' and var_pat['diag_pa'] == 'Si'and var_pat['diag_do'] == 'Si' and var_pat['diag_dg'] =='Si':
        diccionario=diccionario.copy()
        diccionario['resultado']='Otitis'
        diccionario['estado']= True
    elif var_pat['diag_ta'] == 'No' and var_pat['diag_pa'] == 'No'and var_pat['diag_do'] == 'No' and var_pat['diag_dg'] =='No':
        diccionario=diccionario.copy()
        diccionario['resultado']='No sintomas'
        diccionario['estado']= False
    else:
        diccionario=diccionario.copy()
        diccionario['resultado']='Presencia de síntomas'
        diccionario['estado']= False
        
    return(diccionario)
print(diagSintoma({'id_diagnostico':'d-001','diag_ta':'No','diag_pa':'No','diag_do':'No','diag_dg':'Si'}))
