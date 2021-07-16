#Samuel Salcedo Semana 2

def diagSintoma(var_pat) :
    diccionario = {
        'id_diagnostico' : var_pat['id_diagnostico'],
        'resultado': 'enfermedad',
        'estado': 'id_estado'
        }
    if var_pat['diag_ta'] == 'Si':
        if var_pat['diag_pa'] == 'Si':
            if var_pat['diag_do'] == 'Si':
                if var_pat['diag_dg'] =='Si':
                    diccionario=diccionario.copy()
                    diccionario['resultado']='Dengue'
                    diccionario['estado']= True
                    #print(diccionario)
                    

                else:
                    diccionario=diccionario.copy()
                    diccionario['resultado']='Presencia de Sintomas'
                    diccionario['estado']= False
                    #print(diccionario)

            else:
                diccionario=diccionario.copy()
                diccionario['resultado']='Presencia de Sintomas'
                diccionario['estado']= False
                #print(diccionario)


        elif var_pat['diag_do'] == 'No':
            if var_pat['diag_do'] == 'Si':
                diccionario=diccionario.copy()
                diccionario['resultado']='Presencia de Sintomas'
                diccionario['estado']= False
                #print(diccionario)

                
            elif  var_pat['diag_do'] == 'No':
                if var_pat['diag_dg'] == 'Si':
                    diccionario=diccionario.copy()
                    diccionario['resultado']='Gripa'
                    diccionario['estado']= True
                    #print(diccionario)

                else:
                    diccionario=diccionario.copy()
                    diccionario['resultado']='Presencia de Sintomas'
                    diccionario['estado']= False
                    #print(diccionario)

    else:

        if var_pat['diag_pa'] == 'Si':

            if var_pat['diag_do'] == 'Si':

                if var_pat['diag_dg'] =='Si':
                    diccionario=diccionario.copy()
                    diccionario['resultado']='Otitis'
                    diccionario['estado']= True
                    #print(diccionario)
                else:
                    diccionario=diccionario.copy()
                    diccionario['resultado']='Presencia de Sintomas'
                    diccionario['estado']= False
                    #print(diccionario)

            else: 

                diccionario=diccionario.copy()
                diccionario['resultado']='Presencia de Sintomas'
                diccionario['estado']= False
                #print(diccionario)

        else: 
            if (var_pat['diag_do'] or var_pat['diag_dg']) == 'Si':
                diccionario=diccionario.copy()
                diccionario['resultado']='Presencia de Sintomas'
                diccionario['estado']= False
                #print(diccionario)

            else:
                diccionario=diccionario.copy()
                diccionario['resultado']='No tiene sintomas'
                diccionario['estado']= False
                #print(diccionario)
    return(diccionario)
            
#diagSintoma(var_pat)
print(diagSintoma({'id_diagnostico':'d-001','diag_ta':'Si','diag_pa':'No','diag_do':'No','diag_dg':'Si'}))
