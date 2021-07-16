paciente = {
    'id_diagnostico': "5678",
    'diag_ta': 'No',
    'diag_pa': 'No',
    'diag_do': 'No',
    'diag_dg': 'No',
    1: 'Presencia de síntomas',
    2: 'No tiene síntomas'
}


def diagSintoma(paciente: dict) -> dict:

    id_diagnostico = paciente.get('id_diagnostico')
    diag_ta = paciente.get('diag_ta')
    diag_pa = paciente.get('diag_pa')
    diag_do = paciente.get('diag_do')
    diag_dg = paciente.get('diag_dg')

    if (diag_ta == 'Si' and diag_pa == 'Si' and diag_do == 'Si' and diag_dg == 'Si'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Denge', 'estado': True}
    if (diag_ta == 'Si' and diag_pa == 'No' and diag_do == 'No' and diag_dg == 'No'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
    if (diag_ta == 'Si' and diag_pa == 'Si' and diag_do == 'No'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
    if (diag_ta == 'Si' and diag_pa == 'Si' and diag_do == 'Si' and diag_dg == 'No'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
    if (diag_ta == 'Si' and diag_pa == 'No' and diag_do == 'Si'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
    if (diag_ta == 'Si' and diag_pa == 'No' and diag_do == 'No' and diag_dg == 'Si'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Gripa', 'estado': True}

    if (diag_ta == 'No' and diag_pa == 'Si' and diag_do == 'Si' and diag_dg == 'Si'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Otitis', 'estado': True}
    if (diag_ta == 'No' and diag_pa == 'Si' and diag_do == 'No'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
    if (diag_ta == 'No' and diag_pa == 'Si' and diag_do == 'Si' and diag_dg == 'No'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
    if (diag_ta == 'No' and diag_pa == 'No' and diag_do and diag_dg == 'Si'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'Presencia de síntomas', 'estado': False}
    if (diag_ta == 'No' and diag_pa == 'No' and diag_do and diag_dg == 'No'):
        return {'id_diagnostico': id_diagnostico, 'resultado': 'No tiene síntomas', 'estado': False}


print(diagSintoma(paciente))
