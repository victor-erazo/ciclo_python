diagnostico1 = {'id_diagnostico':'d-001','diag_ta':'Si','diag_pa':'No','diag_do':'No','diag_dg':'Si'} #gripa


def diagSintoma(dicc_diagnostico):

    valores_rta = ['id_diagnostico','resultado','estado']
    r = dict.fromkeys(valores_rta)
    r['id_diagnostico'] = dicc_diagnostico['id_diagnostico']

    if dicc_diagnostico['diag_ta'] == 'Si':

        if dicc_diagnostico['diag_pa'] == 'Si'and dicc_diagnostico['diag_do'] == 'Si' and dicc_diagnostico['diag_dg'] == 'Si':
                        
            r['resultado'] = 'Dengue'
            r['estado'] = True
            return r
                
        if dicc_diagnostico['diag_pa'] == 'Si':

            if dicc_diagnostico['diag_do'] == 'No':
                #de presion alta y temp alta
                
                r['resultado'] = 'Presencia de síntomas'
                r['estado'] = False
                return r

            else: # si ademas de dolor de oido
                if dicc_diagnostico['diag_dg'] == 'No': 
                    # temp alta + presion alta + dolor de oido
                    
                    r['resultado'] = 'Presencia de síntomas'
                    r['estado'] = False
                    return r

        else: #si no tiene la presion alta pero sigue con temp alta:
        
            if dicc_diagnostico['diag_do'] == 'Si':
                # temp alta + dolor de oido
                
                r['resultado'] = 'Presencia de síntomas'
                r['estado'] = False
                return r
            else:
                if dicc_diagnostico['diag_dg'] == 'Si':
                    
                    r['resultado'] = 'Gripa'
                    r['estado'] = True
                    return r
                else:
                    # solo temp alta.
                    
                    r['resultado'] = 'Presencia de síntomas'
                    r['estado'] = False
                    return r
                
    else:
        if dicc_diagnostico['diag_pa'] == 'Si' and dicc_diagnostico['diag_do'] == 'Si' and dicc_diagnostico['diag_dg'] == 'Si':
                        
            r['resultado'] = 'Otitis'
            r['estado'] = True
            return r
                    
        if dicc_diagnostico['diag_pa'] == 'Si':
         
            if dicc_diagnostico['diag_do'] == 'No':
                                
                r['resultado'] = 'Presencia de síntomas'
                r['estado'] = False
                return r # solamente presion alta

            else: # si tienen dolor de oido
                if dicc_diagnostico['diag_dg'] == 'No':
                                        
                    r['resultado'] = 'Presencia de síntomas'
                    r['estado'] = False
                    return r # presion alta y de dolor de oido
        else:
            if dicc_diagnostico['diag_do'] and dicc_diagnostico['diag_dg'] == 'Si':
                                
                r['resultado'] = 'Presencia de síntomas'
                r['estado'] = False
                return r #dolor de oido o de garganta
            else:
                r['resultado'] = 'No tiene síntomas'
                r['estado'] = False
                return r