import streamlit as st

# Configuração inicial do app
st.set_page_config('Carga de Gás em Ar-Condicionado', page_icon=':mechanic:')
st.title('AR-CONDICIONADO')
st.title('Carga Adicional de Fluido Refrigerante :material/fluid:')

parametros = {
    'AGRATTO':{
        '9 a 12.000 BTU/h':{
            'capacidade': '9 a 12.000 BTU/h',
            'R-32': {'carga_por_metro':20, 'limite_fabrica': 5.0, 'limite_maximo': 15.0, 'limite_minimo': 2.0}
        },
        '18.000 BTU/h':{
            'capacidade': '18.000 BTU/h',
            'R-32': {'carga_por_metro':20, 'limite_fabrica': 5.0, 'limite_maximo':15.0, 'limite_minimo': 2.0}
        },
        '22.000 BTU/h':{
            'capacidade': '22.000 BTU/h',
            'R-32': {'carga_por_metro':20, 'limite_fabrica': 5.0, 'limite_maximo':15.0, 'limite_minimo': 2.0}
        },
        '24.000 BTU/h':{
            'capacidade': '24.000 BTU/h',
            'R-32': {'carga_por_metro':20, 'limite_fabrica': 5.0, 'limite_maximo':15.0, 'limite_minimo': 2.0}
        },
        '30.000 BTU/h':{
            'capacidade': '30.000 BTU/h',
            'R-32': {'carga_por_metro':20, 'limite_fabrica': 5.0, 'limite_maximo':15.0, 'limite_minimo': 2.0}
        },       
        
    },
    
    'DAIKIN': {
       '9 a 12.000 BTU/h': {
           'capacidade': '9 a 12.000 BTU/h',
           'R-32': {'carga_por_metro': 20, 'limite_fabrica': 10.0, 'limite_minimo': 3.0, 'limite_maximo': 15.0}
       },
       '18.000 BTU/h': {
           'capacidade': '18.000 BTU/h',
           'R-32': {'carga_por_metro': 0, 'limite_fabrica': 15.0, 'limite_minimo': 3.0, 'limite_maximo': 15.0}
       },
       '24.000 BTU/h': {
           'capacidade': '24.000 BTU/h',
           'R-32': {'carga_por_metro': 20, 'limite_fabrica': 10, 'limite_minimo': 3.0, 'limite_maximo': 30.0}
       }
    },
    'ELECTROLUX': {
        '9 a 12.000 BTU/h': {
            'capacidade': '9 a 12.000 BTU/h',
            'R-32': { 'carga_por_metro': 12,
            'limite_fabrica': 8.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0}
           
        },
        '18.000 BTU/h': {
            'capacidade': '18.000 BTU/h',
            'R-32': {
            'carga_por_metro': 12,
            'limite_fabrica': 10.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0
            }

        },
        '24.000 BTU/h': {
            'capacidade': '24.000 BTU/h',
            'R-32': {
            'carga_por_metro': 12,
            'limite_fabrica': 10.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0
            }
           
        }
    },
    'ELGIN': {
        '9 a 12.000 BTU/h': {
            'capacidade': '9 a 12.000 BTU/h',
            'R-32': { 'carga_por_metro': 20,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15}
           
        },
        '18.000 BTU/h': {
            'capacidade': '18.000 BTU/h',
            'R-32': { 'carga_por_metro': 25,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 20.0}
        },
        '24.000 BTU/h': {
            'capacidade': '24.000 BTU/h',
            'R-32': {'carga_por_metro': 25,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 20.0}         
        },
        '30.000 BTU/h': {
            'capacidade': '30.000 BTU/h',
            'R-32': {'carga_por_metro': 25,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 20.0} 
        },
        
    },
    'FUJITSU AIRSTAGE': {
        '9 a 12.000 BTU/h': {
            'capacidade': '9 a 12.000 BTU/h',
            'R-32': {
            'carga_por_metro': 20,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0
            }
            
        },
        '18.000 BTU/h': {
            'capacidade': '18.000 BTU/h',
            'R-32': {
            'carga_por_metro': 20,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0
            }
        },
        '24.000 BTU/h': {
            'capacidade': '24.000 BTU/h',
            'R-32': {
            'carga_por_metro': 30,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0
            }
        },
        '30.000 BTU/h': {
            'capacidade': '30.000 BTU/h',
            'R-32': {
            'carga_por_metro': 40,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0
            }
        },
        '36.000 BTU/h': {
            'capacidade': '36.000 BTU/h',
            'R-32': {
            'carga_por_metro': 40,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0
            }
        },
    },
    'LG': {
        '9 a 12.000 BTU/h': {
            'capacidade': '9 a 12.000 BTU/h',
            'R-32': {
            'carga_por_metro': 20,
            'limite_fabrica': 7.5,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0
            }          
        },
        '19.000 BTU/h': {
            'capacidade': '19.000 BTU/h',
            'R-32': {
            'carga_por_metro': 20,
            'limite_fabrica': 7.5,
            'limite_minimo': 3.0,
            'limite_maximo': 20.0
            }
            
        },
        '22.000 BTU/h': {
            'capacidade': '22.000 BTU/h',
            'R-32': {
            'carga_por_metro': 20,
            'limite_fabrica': 7.5,
            'limite_minimo': 3.0,
            'limite_maximo': 20.0
            }   
        }, 
         '30.000 BTU/h': {
            'capacidade': '30.000 BTU/h',
            'R-32': {
            'carga_por_metro': 30,
            'limite_fabrica': 7.5,
            'limite_minimo': 5.0,
            'limite_maximo': 30.0
            }          
        },
         '36.000 BTU/h': {
            'capacidade': '36.000 BTU/h',
            'R-32': {
            'carga_por_metro': 30,
            'limite_fabrica': 7.5,
            'limite_minimo': 5.0,
            'limite_maximo': 30.0
            }          
        },
            
        },
    'MIDEA': {
        '9 a 12.000 BTU/h': {
            'capacidade': '9 a 12.000 BTU/h',            
            'R-32': {'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'fluido': 'R-32',
            'limite_minimo': 2.0,
            'limite_maximo': 25.0
        },          
        },          
        '18.000 BTU/h': {
            'capacidade': '18.000 BTU/h',
            'R-32': {'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'fluido': 'R-32',
            'limite_minimo': 2.0,
            'limite_maximo':30.0
        },          
        },
        '24.000 BTU/h': {
            'capacidade': '24.000 BTU/h',
            'R-32': {'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'fluido': 'R-32',
            'limite_minimo': 2.0,
            'limite_maximo':30.0
        },          
        },
    },
    'SAMSUNG': {
        '9 a 12.000 BTU/h': {
            'capacidade': '9 a 12.000 BTU/h',
            'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0
            }
         },
        '18.000 BTU/h': {
            'capacidade': '18.000 BTU/h',
             'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 30.0
            }
        },
        '24.000 BTU/h': {
            'capacidade': '24.000 BTU/h',
            'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 30.0
            }
        },
    },
    'TCL': {
        '9 a 12.000 BTU/h': {
            'capacidade': '9 a 12.000 BTU/h',
            'R-410A': {
            'carga_por_metro':20,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0
            }
        },
        '18.000 BTU/h': {
            'capacidade': '18.000 BTU/h',
            'R-410A': {
            'carga_por_metro':30,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0
            }
        },
        '24.000 BTU/h': {
            'capacidade': '24.000 BTU/h',
            'R-410A': {
            'carga_por_metro':30,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0
            }
        },
        '32.000 BTU/h': {
            'capacidade': '32.000 BTU/h',
            'R-410A': {
            'carga_por_metro':30,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0
            }
        },
        
        
        
        
    }
}

# Função para calcular a carga total em BTUs
def calcular_carga_total(metros, fabricante, capacidade, gas):
    try:
        carga_por_metro = parametros[fabricante][capacidade][gas]['carga_por_metro']
        carga_total = carga_por_metro * metros
        
        # Adicionar lógica para a quantidade de gás
        if fabricante == 'AGRATTO':
            if capacidade in ['9 a 12.000 BTU/h', '18.000 BTU/h', '22.000 BTU/h', '24.000 BTU/h', '30.000 BTU/h']:
                if metros <= 5:
                    st.info(f'Para {metros} metros, não é necessário adicionar gás.')
                    return carga_total
                elif metros > 5 and metros <= 15:
                    carga_adicional = (metros - 5) * 20   
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
          
        if fabricante == 'DAIKIN':
            if capacidade in ['9 a 12.000 BTU/h', '24.000 BTU/h']:
                if metros <= 10:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 10 and metros <= 15:
                    # Adicionar 20g de gás para cada metro acima de 10m
                    carga_adicional = (metros - 10) * 20  # Adicionando 20g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                elif metros > 15:
                    # Adicionar 20g de gás para cada metro acima de 15m
                    carga_adicional = (metros - 10) * 20  # Adicionando 20g por metro acima de 15m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
            elif capacidade == '18.000 BTU/h':
                # Para 18.000 BTU/h, não é necessário adicionar gás até 15m
                if metros <= 15:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 15:
                    # Adicionar lógica se for necessário adicionar gás
                    st.warning(f"Para {metros} metros, considere adicionar gás, pois a tubulação ultrapassou 15 metros.")
        
        # Lógica para ELECTROLUX
        elif fabricante == 'ELECTROLUX':
            if capacidade == '9 a 12.000 BTU/h':
                if metros <= 8:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 8 and metros <= 15:
                    carga_adicional = (metros - 8) * 12  # Adicionando 12g por metro acima de 8m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_total} gramas.")
                else:
                    st.warning(f"Para {metros} metros, considere adicionar gás, pois a tubulação ultrapassou 15 metros.")

            elif capacidade == '18.000 BTU/h':
                if metros <= 10:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 10) * 12 # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
            
            elif capacidade == '24.000 BTU/h':
                if metros <= 10:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 10) * 12  # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")                
                    
        # Lógica para ELGIN
        elif fabricante == 'ELGIN':
            if capacidade == '9 a 12.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 5 and metros <= 15:
                    carga_adicional = (metros - 5) * 20  # Adicionando 12g por metro acima de 8m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                else:
                    st.warning(f"Para {metros} metros, considere adicionar gás, pois a tubulação ultrapassou 15 metros.")

            elif capacidade == '18.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 5) * 25 # Adicionando 25g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
            
            elif capacidade == '24.000 BTU/h' or capacidade == '30.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 5) * 25  # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                    
        # Lógica para FUJITSU AIRSTAGE
        elif fabricante == 'FUJITSU AIRSTAGE':
            if capacidade == '9 a 12.000 BTU/h' or capacidade == '18.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 5 and metros <= 15:
                    carga_adicional = (metros - 5) * 20  # Adicionando 12g por metro acima de 8m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                else:
                    st.warning(f"Para {metros} metros, considere adicionar gás, pois a tubulação ultrapassou 15 metros.")

            elif capacidade == '24.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 5) * 30 # Adicionando 25g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
            
            elif capacidade == '30.000 BTU/h' or capacidade == '36.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 5) * 40  # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")            
         
        # Lógica para LG
        elif fabricante == 'LG':
            if capacidade == '9 a 12.000 BTU/h':
                if metros <= 7.5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 7.5 and metros <= 15:
                    carga_adicional = (metros - 7.5) * 20  
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                
            elif capacidade == '19.000 BTU/h':
                if metros <= 7.5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 7.5) * 20 # Adicionando 25g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                    
            elif capacidade == '22.000 BTU/h':
                if metros <= 7.5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 7.5) * 20 # Adicionando 25g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
            
            elif capacidade == '30.000 BTU/h' or capacidade == '36.000 BTU/h':
                if metros <= 7.5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 7.5) * 30  # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.") 
                         
        # Lógica para SPRINGER-MIDEA
        elif fabricante == 'MIDEA':
            if capacidade == '9 a 12.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 5 and metros <= 15:
                    carga_adicional = (metros - 5) * 15  # Adicionando 12g por metro acima de 8m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                else:
                    st.warning(f"Para {metros} metros, considere adicionar gás, pois a tubulação ultrapassou 15 metros.")

            elif capacidade == '18.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 5) * 15 # Adicionando 25g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
            
            elif capacidade == '24.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 5) * 15  # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
        
        # Lógica para SAMSUNG
        elif fabricante == 'SAMSUNG':
            if capacidade == '9 a 12.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 5 and metros <= 15:
                    carga_adicional = (metros - 5) * 15  # Adicionando 12g por metro acima de 8m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                else:
                    st.warning(f"Para {metros} metros, considere adicionar gás, pois a tubulação ultrapassou 15 metros.")

            elif capacidade == '18.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 5) * 15 # Adicionando 25g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
            
            elif capacidade == '24.000 BTU/h':
                if metros <= 5:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 5) * 15  # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")   
    
        # Lógica para TCL
        elif fabricante == 'TCL':
            if capacidade == '9 a 12.000 BTU/h':
                if metros <= 3:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total  # Retorna apenas a carga total sem gás
                elif metros > 3 and metros <= 15:
                    carga_adicional = (metros - 3) * 20  # Adicionando 12g por metro acima de 8m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
                else:
                    st.warning(f"Para {metros} metros, considere adicionar gás, pois a tubulação ultrapassou 15 metros.")

            elif capacidade == '18.000 BTU/h':
                if metros <= 3:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 3) * 30 # Adicionando 25g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")
            
            elif capacidade == '24.000 BTU/h':
                if metros <= 3:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 3) * 30  # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")  
                    
            elif capacidade == '32.000 BTU/h':
                if metros <= 3:
                    st.info(f"Para {metros} metros, não é necessário adicionar gás.")
                    return carga_total
                else:
                    carga_adicional = (metros - 3) * 30  # Adicionando 15g por metro acima de 10m
                    carga_total += carga_adicional
                    st.success(f"A carga total para {metros} metros com o modelo {fabricante}, capacidade {capacidade} e gás {gas} é: {carga_adicional} gramas.")  
                    
                    
                  
        return carga_total
    except KeyError:
        return None
    
# Função para obter informações sobre limites
def obter_limites(fabricante, capacidade, gas):
    try:
        limite_minimo = parametros[fabricante][capacidade][gas]['limite_minimo']
        limite_maximo = parametros[fabricante][capacidade][gas]['limite_maximo']
        return limite_minimo, limite_maximo
    except KeyError:
        return None, None

# Entrada do usuário
fabricante = st.selectbox("Escolha o fabricante:", options=list(parametros.keys()))
metros = st.number_input("Insira o total de metros de tubulação:", min_value=0.0)

# Escolha a capacidade do modelo
capacidade = st.selectbox("Escolha a capacidade:", options=list(parametros[fabricante].keys()))

# Escolha o tipo de gás
if fabricante and capacidade:
    gases_disponiveis = list(parametros[fabricante][capacidade].keys())
    gas = st.selectbox('Escolha o tipo de gás', gases_disponiveis, index=1)

# Exibir limites de comprimento
limite_minimo, limite_maximo = obter_limites(fabricante, capacidade, gas)
if limite_minimo is not None and limite_maximo is not None:
    st.warning(f"Comprimento mínimo da tubulação: {limite_minimo} metros")
    st.warning(f"Comprimento máximo da tubulação: {limite_maximo} metros")

 # Botão para calcular
    if st.button("Calcular Carga Total"):
        if metros < limite_minimo or metros > limite_maximo:
            st.error(f"O comprimento deve estar entre {limite_minimo} e {limite_maximo} metros.")
        else:
            carga_total = calcular_carga_total(metros, fabricante, capacidade, gas)

else:
    st.warning("Por favor, selecione um fabricante e uma capacidade antes de escolher o gás.")

        
        