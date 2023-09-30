import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import base64
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os


#st.title('Plataformas electorales nacionales de las agrupaciones politicas')

with open("data/LLA.pdf","rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="650" height="1000" type="application/pdf"></iframe>'

with open("data/JxC.pdf","rb") as f:
    base64_pdf2 = base64.b64encode(f.read()).decode('utf-8')

pdf_display2 = f'<iframe src="data:application/pdf;base64,{base64_pdf2}" width="650" height="1000" type="application/pdf"></iframe>'

with open("data/UxP.pdf","rb") as f:
    base64_pdf3 = base64.b64encode(f.read()).decode('utf-8')

pdf_display3 = f'<iframe src="data:application/pdf;base64,{base64_pdf3}" width="650" height="1000" type="application/pdf"></iframe>'

st.markdown("<h1 style='text-align: center;'>Propuestas de los candidatos presidenciales</h1>", unsafe_allow_html=True)

fit1, fit2, fit3= st.columns([0.2, 0.6, 0.2])
with fit2:
    
    st.markdown("<h2 style='text-align: center;'>Javier Milei (La Libertad Avanza)</h2>", unsafe_allow_html=True)
    with st.expander('📈 **Economía**'):
         st.write("<br> **Establecer una reforma tributaria y previsional:** que empuje una baja de los impuestos para potenciar el desarrollo de los procesos productivos que lleva adelante la actividad privada y potenciar la exportación de bienes y servicios. Recortar el gasto del Estado en jubilaciones y pensiones, de los ítems que más empujan el déficit fiscal alentando un sistema de capitalización privado y una apertura unilateral al comercio internacional. Aumentar la flexibilización laboral para la creación de empleos en el sector privado. Eliminar progresivamente los planes sociales a medida que se generen otros ingresos como la consecuencia de la creación de puestos de trabajo en el sector privado.<br><br> **Liquidar el Banco Central de la República Argentina y liberar inmediatamente todos los cepos cambiarios:** establecer un sistema de banca Simons, con encajes al 100% para depósitos a la vista. Unificar el tipo de cambio y establecer un sistema de monedas competitivo que permita a los ciudadanos elegir el sistema monetario libremente o la dolarización de la economía.<br><br> **Privatizar empresas públicas deficitarias**", unsafe_allow_html=True)
    with st.expander('📜 **Democracia**'):
      st.write("<br> Promover la libertad de afiliación sindical e incentivar la limitación temporal de los mandatos sindicales<br><br> Poner fin a la industria del juicio<br><br> Crear un plan de retiro voluntario para empleados públicos con el fin de achicar el Estado<br><br> Reducir la cantidad de ministerios a 8", unsafe_allow_html=True) 
    with st.expander('⚕️ **Salud**'):
      st.write("<br> Reformar profundamente el sistema de salud con impulso del sistema privado, competitividad libre entre empresas del sector y mejorar la estructura edilicia hospitalaria<br><br>  Arancelar todas las prestaciones y auto gestionar el servicio de salud el servicio de salud en trabajos compartidos con la salud privada<br><br>  Proteger al niño desde la concepción<br><br>  Modificar la Ley de Salud Mental y desarrollar programas de prevención para los trastornos adictivos, educativos y de la personalidad<br><br>  Regular la documentación de extranjeros que trabajen en salud y exigir a los turistas extranjeros que cuenten con un seguro de salud ", unsafe_allow_html=True)
    with st.expander('📖 **Educación**'):
      st.write("<br> Descentralizar la educación entregando el presupuesto a los padres, en lugar de dárselo al ministerio, financiando la demanda<br><br>  Generar competencia entre las instituciones educativas desde lo curricular en todos los niveles de educación, incorporando más horas de materias como matemática, lengua, ciencias, tic o por la orientación y/o infraestructura<br><br>  Promover una transformación curricular donde se promueva un enfoque pedagógico por habilidades, que va más allá de la simple transmisión del conocimiento. Aplicando modificaciones que orienten a los estudiantes a las profesiones necesarias para el país (ingenieros, informáticos)<br><br>  Crear la carrera docente de nivel universitario y la carrera de directivos y supervisores<br><br>  Eliminar la obligatoriedad de la ESI en todos los niveles de enseñanza", unsafe_allow_html=True)
    with st.expander('♻️ **Ambiente**'):
      st.write("<br> Invertir en el mantenimiento del sistema energético actual y promover nuevas fuentes de energías renovables y limpias (solar, eólica, hidrógeno verde, etc)<br><br> Fomentar la creación de centros de reciclaje de residuos para su transformación en energía y materiales reutilizables<br><br> Profundizar la investigación en energía nuclear a fin de elaborar generadores nucleares de industria nacional para la generación de energía y exportación<br><br> Promover una agricultura de buenas prácticas contemplando sustentabilidad del suelo y la preservación del medioambiente.<br><br> Reformular el sistema de Emergencia Agropecuaria y cuidar nuestro patrimonio marítimo evitando el aprovechamiento indiscriminado e ilegal", unsafe_allow_html=True)
    with st.expander('👮‍♂️ **Seguridad**'):
      st.write("<br> Construir establecimientos penitenciarios con sistema de gestión público-privada y eliminar los salarios de los reclusos a través de una modificación de la legislación.<br><br> Prestar especial atención a la lucha contra el narcotráfico, atacando cada una de las células y organizaciones delictivas, controlando límites provinciales y espacio aéreo con radares y personal calificado, dotando a su personal de conocimiento, herramientas de trabajo, de protección junto con el manejo de y aplicación de las nuevas tecnologías<br><br> Disminuir la dificultad del accionar policial a través de la modificación de las leyes y la presentación de nuevos proyectos de ley y sanear todas las fuerzas de seguridad, haciendo eje en la lucha contra la corrupción<br><br> Prohibir el ingreso al país de extranjeros con antecedentes penales y deportar inmediatamente a extranjeros que cometan delitos en el país<br><br> Promover una doctrina de Seguridad Nacional y sus estrategias", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Sergio Massa (Unión por la Patria)</h2>", unsafe_allow_html=True)
    with st.expander('📈 **Economía**'):
         st.write("Romper con el FMI: decirle no al pago de la deuda y usar esa plata para pagar salarios, generar trabajo y garantizar el acceso a la salud, educación y vivienda.<br><br>Nacionalizar la banca y el comercio exterior, estatizar todas las privatizadas: evitar la fuga de capitales y estatizar privadas de servicios bajo el control de sus trabajadores y usuarios junto con técnicos y especialistas de la universidades públicas.<br><br>Cuidar a los pequeños ahorristas y brindar créditos baratos<br><br>Aumentar salarios, jubilaciones, anular la reforma previsional y prohibir despidos y suspensiones: el ingreso mensual debe cubrir las necesidades básicas. Expropiar y estatizar empresas en crisis para que sean puestas a producir, bajo el control de sus trabajadores y trabajadoras. Eliminar trabajo precario y en negro, todos y todas a planta permanente. Rechazar nuevas formas de explotación laboral a través de plataformas virtuales. 82% móvil para los jubilados y jubiladas. <br><br>Eliminar el IVA de la canasta familiar: Abolir el impuesto al salario.", unsafe_allow_html=True)
    with st.expander('📜 **Democracia**'):
      st.write("Hacer que los funcionarios ganen como una maestra o un obrero especializado: que los propios electores y electoras puedan revocar los mandatos de estos funcionarios y funcionarias. Rechazar los dietazos de los legisladores y jueces. ", unsafe_allow_html=True) 
    with st.expander('⚕️ **Salud**'):
      st.write("Garantizar el acceso a la salud: usando la plata del pago de la deuda al FMI<br><br>Unificar y centralizar el sistema de salud: reunir la totalidad de los recursos del sistema público, privado, de obras sociales y de la Universidad, bajo control de los trabajadores y profesionales. Implementar comités de emergencia central y locales, con participación de los y las trabajadores/as. ", unsafe_allow_html=True)
    with st.expander('📖 **Educación**'):
      st.write("", unsafe_allow_html=True)
    with st.expander('♻️ **Ambiente**'):
      st.write("", unsafe_allow_html=True)
    with st.expander('👮‍♂️ **Seguridad**'):
      st.write("", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Patricia Bullrich (Juntos por el Cambio)</h2>", unsafe_allow_html=True)
    with st.expander('📈 **Economía**'):
         st.write("<br> Ir a un bimonetarismo y sacar el cepo cambiario que disminuye las reservas e impide exportar e importar en una economía libre que promueva las inversiones productivas. Confiar en una ingeniería jurídica que evite una explosión de la economía.<br><br> Bajar la inflación bajando la emisión monetaria, con solidez fiscal, un Banco Central independiente, una reforma del Estado y laboral, cambios impositivos y un pacto federal.<br><br> Convertir los planes sociales en seguros de desempleo y que en 4 años dejen de existir los planes sociales, reemplazandolos con empleo. Fomentar la dispersión territorial hacia ciudades más amables con la generación de polos de desarrollo por fuera del Conurbano.Crear un Pacto Federal para reducir impuestos improductivos para economías regionales y discutir la distribución de los subsidios hacia la Capital Federal.<br><br> Terminar con las restricciones a las importaciones para evitar que retrase y estanque el progreso. Promover que el campo crezca libremente y aumente las exportaciones. Promover las exportaciones de la pesca, la minería, la industria y todos los sectores.<br><br> Achicar del Estado y congelar contrataciones. Pasar de 23 ministerios ineficientes a 8-10. Reducir la burocracia estatal, el gasto en personal sin tareas específicas y mejorar salarios del personal esencial como policías, médicos y docentes. Definir un plazo para que las empresas públicas presenten un plan de negocios con déficit cero. Si no, serán privatizadas o reconvertidas en cooperativas.", unsafe_allow_html=True)
    with st.expander('📜 **Democracia**'):
      st.write("<br> Transparentar las campañas electorales. Generar mecanismos más fuertes para evitar el uso de recursos públicos en campañas electorales que alimentan el clientelismo. Limitar movilizaciones y piquetes. Crear leyes que pongan límites a las movilizaciones y la toma de calles para que dejen de ser un elemento permanente.<br><br> Lograr que todas las provincias tengan regímenes electorales razonables, instituciones de la transparencia y que el poder político no tome presa a la justicia.<br><br> Achicar del Estado y congelar contrataciones. Pasar de 23 ministerios ineficientes a 8-10. Reducir la burocracia estatal, el gasto en personal sin tareas específicas y mejorar salarios del personal esencial como policías, médicos y docentes. Definir un plazo para que las empresas públicas presenten un plan de negocios con déficit cero. Si no, serán privatizadas o reconvertidas en cooperativas.", unsafe_allow_html=True) 
    with st.expander('⚕️ **Salud**'):
      st.write("<br> La fuente seleccionada no presenta propuestas.", unsafe_allow_html=True)
    with st.expander('📖 **Educación**'):
      st.write("<br> Cumplir 190 días efectivos de clase y plantear un compromiso de los próximos 12 años con una generación completa de estudiantes que no pierda días de clases.<br><br> Implementar un examen de ingreso para docentes secundarios y universitarios, con exámenes regulares a docentes en función para asegurar un buen nivel educativo. Desregular la actividad docente para incorporar otros formadores profesionales en cuestiones como informática y nuevas tecnologías, incorporándolos a la actividad docente con un curso de pedagogía.<br><br> Rearmar la currícula educativa sin adoctrinamiento para enseñar con información objetiva en las aulas. Liberar a los docentes de los sindicatos. Salir de la lógica de los paros permanentes y llamar a una nueva épica educativa.", unsafe_allow_html=True)
    with st.expander('♻️ **Ambiente**'):
      st.write("<br> La fuente seleccionada no presenta propuestas.", unsafe_allow_html=True)
    with st.expander('👮‍♂️ **Seguridad**'):
      st.write("<br> Quitar planes sociales a quienes hagan piquetes.<br><br> Tener mano firme en el combate con el delito: modificar el código penal elevando las penas de narcotráfico, abusos, homicidios y todos los delitos graves.<br><br> Hacer cumplir la ley, que los presos no salgan de las cárceles de forma anticipada. Bajar la edad de imputabilidad a los 14 años de edad y que exista para chicos con menos de catorce años un tratamiento en el que se trabaje la toma de conciencia del daño cometido en el delito, para que no arruinen sus vidas, ni la de los otros.<br><br> Darle a las fuerzas armadas el lugar que les corresponde para que dejen de estar de lado y trabajen al servicio del país.", unsafe_allow_html=True)   

    st.markdown("<h2 style='text-align: center;'>Juan Schiaretti (Hacemos por Nuestro País)</h2>", unsafe_allow_html=True)
    with st.expander('📈 **Economía**'):
         st.write("<br> **Bajar la inflación con un plan integral de estabilización:** prudencia y disciplina en la emisión monetaria, equilibrio fiscal, recomposición de reservas, defensa de la competencia, incentivo a las inversiones y una inteligente política de ingresos.<br><br>**Establecer un sistema tributario simple, estable y progresivo:** conseguir un sistema tributario que no penalice la producción con malos impuestos, eliminar de manera gradual las retenciones a exportaciones y alentar con los ingresos fiscales la inversión productiva con creación de empleo.<br><br>**Generar una moneda nacional:** una moneda nacional sana y fuerte como condición estructural para la estabilidad económica.<br><br>**Realizar un proyecto de desarrollo integral:** permitir desplegar la potencialidad de nuestros recursos humanos y naturales, impulsar la capacidad innovadora de las personas como base para un compromiso armonioso con las empresas, sindicatos, universidades y complejo científico-tecnológico.<br><br>**Garantizar una nueva política tributaria para las Pymes y establecer un sistema simple y accesible de créditos a las producción:** alentar la inversión con empleo, incentivos tributarios para que se reviertan utilidades en bienes de capital", unsafe_allow_html=True)
    with st.expander('📜 **Democracia**'):
      st.write("<br> **Respetar la independencia del poder judicial:** pleno derecho a la división de poderes, sin avasallamiento de uno sobre el otro, respetando la independencia del poder judicial.<br><br> **Fortalecer la institucionalidad republicana y potenciar la transparencia:** postular reglas claras, sencillas y estables para quienes producen, investigan o invierten. Emplear una plena rendición de cuentas con participación ciudadana.<br> **Establecer un estricto criterio federal:** definir transporte, energía, conectividad y logística con criterio federal. ", unsafe_allow_html=True) 
    with st.expander('⚕️ **Salud**'):
      st.write("<br> **Avanzar en la digitalización de la medicina:** Promover la telemedicina para lograr un acceso real de forma eficaz y rápida, brindando una atención permanente y especializada a pesar de las distancias en todas las ciudades del país. También se debe avanzar en un sistema que permita pedir un turno o consultar resultados desde el celular o computadora, para no tener que hacer colas en la madrugada para conseguir un turno. Además se debe generar una única historia clínica digital, esta mejora la atención y baja los costos de salud al dar acceso a toda la información en todo momento.<br><br> **Mejorar la atención de los problemas de salud mental y bienestar emocional:** Se va a promover la modificación de la ley de salud mental para adaptarla a las necesidades actuales. Además es fundamental que los profesionales que están en la primera línea de fuego para la detección de los problemas de salud mental, se capaciten para mejorar la detección, resolución o derivación a centros especializados para su tratamiento o rehabilitación.<br><br> **Jerarquizar a los profesionales de salud:** Establecer estándares mínimos de condiciones laborales para los profesionales de salud, generando incentivos específicos para la radicación de profesionales en todo el país, en particular las áreas más desatendidas, como las zonas rurales, así como promover el desarrollo de las especialidades cuyo déficit es cada vez más pronunciado, lo que está afectando la atención médica tanto en el sector público como en el privado a lo largo y ancho de nuestro territorio.<br><br> **Mejorar la atención primaria en salud:** Invertir en infraestructura, profesionales, tecnología y financiamiento para que cada argentino pueda acceder a un centro de salud con cuidados continuados y se favorezca la participación social en el cuidado de la salud. Poner foco en la salud materno-infantil, la vacunación y nutrición, las enfermedades transmisibles, la adopción de estilos de vida saludables y la prevención y control de enfermedades crónicas, que hoy dan cuenta de más de 7 de cada 10 muertes en nuestro país.<br><br> **Promover la articulación e integración de los subsectores de la salud:** Garantizar en un mismo paquete todas las prestaciones con eficiencia, equidad y acreditación de la calidad, tanto en el sector público de las provincias, como en todas las obras sociales, las empresas de medicina prepaga, la red de hospitales, las clínicas y los sanatorios privados.", unsafe_allow_html=True)
    with st.expander('📖 **Educación**'):
      st.write("<br> **Reconstruir un verdadero sistema nacional de educación y garantizar calidad educativa:** fortalecer el federalismo integrando diferencias y poniendo equilibrio donde hay desigualdad.<br><br>  **Garantizar la ampliación de la jornada extendida en nivel primario:** incluyendo idiomas y robótica en todas las escuelas. Volver esencial a la tecnología digital en el aprendizaje y fortalecer el aprendizaje de las ciencias básicas.<br><br> **Jerarquizar la función docente:** con remuneraciones justas y formación permanente.<br><br>  **Crear un “cuarto nivel educativo”:** destinado a jóvenes y adultos, asociado al mundo del trabajo y la formación laboral.", unsafe_allow_html=True)
    with st.expander('♻️ **Ambiente**'):
      st.write("<br> **Sostener esfuerzos por frenar la deforestación:** llevar a ceros en términos netos en el año 2030. Garantizar la eliminación de plásticos de un solo uso de manera inmediata.<br><br> **Cumplir los objetivos de emisiones de GEI del Acuerdo de París:** aumentar gradualmente el corte de combustibles tradicional con bioetanol y con biodiesel.<br><br> **Revalorizar al Mar Argentino en la economía nacional:** incorporar a la matriz productiva e industrial al Mar como actor protagónico, en el desarrollo y explotación de la plataforma marítima, sin dejar de lado el cuidado del ambiente.", unsafe_allow_html=True)
    with st.expander('👮‍♂️ **Seguridad**'):
      st.write("<br> **Promover el desarme de la ciudadanía:** evitar la circulación de armas ilegales.<br><br> **Crear un Consejo Federal para el mejoramiento de la Justicia Federal:** poner en marcha el sistema acusatorio en todo el territorio nacional, inmediata implementación del juicio por jurado, entre otras.<br><br> **Contar con más efectivos en las fuerzas federales:** cuidar la frontera y combatir al narcotráfico.<br><br> **Reformular el trabajo de inteligencia criminal y análisis del delito:** incorporar tecnología y coordinación entre las fuerzas de seguridad, justicia y diversas agencias del Estado.", unsafe_allow_html=True)   

    st.markdown("<h2 style='text-align: center;'>Myriam Bregman (Frente de Izquierda)</h2>", unsafe_allow_html=True)

    with st.expander('📈 **Economia**'):
         st.write("<br> **Romper con el FMI:** decirle no al pago de la deuda y usar esa plata para pagar salarios, generar trabajo y garantizar el acceso a la salud, educación y vivienda.<br><br> **Nacionalizar la banca y el comercio exterior, estatizar todas las privatizadas:** evitar la fuga de capitales y estatizar privadas de servicios bajo el control de sus trabajadores y usuarios junto con técnicos y especialistas de la universidades públicas. Cuidar a los pequeños ahorristas y brindar créditos baratos. <br><br> **Aumentar salarios, jubilaciones, anular la reforma previsional y prohibir despidos y suspensiones:** el ingreso mensual debe cubrir las necesidades básicas. Expropiar y estatizar empresas en crisis para que sean puestas a producir, bajo el control de sus trabajadores y trabajadoras. Eliminar trabajo precario y en negro, todos y todas a planta permanente. Rechazar nuevas formas de explotación laboral a través de plataformas virtuales. 82% móvil para los jubilados y jubiladas. <br><br> **Eliminar el IVA de la canasta familiar:** Abolir el impuesto al salario.", unsafe_allow_html=True)
    with st.expander('📜 **Democracia**'):
      st.write("<br> **Hacer que los funcionarios ganen como una maestra o un obrero especializado:** que los propios electores y electoras puedan revocar los mandatos de estos funcionarios y funcionarias. Rechazar los dietazos de los legisladores y jueces. ", unsafe_allow_html=True) 
    with st.expander('⚕️ **Salud**'):
      st.write("<br> **Garantizar el acceso a la salud:** usando la plata del pago de la deuda al FMI<br><br> **Unificar y centralizar el sistema de salud:** reunir la totalidad de los recursos del sistema público, privado, de obras sociales y de la Universidad, bajo control de los trabajadores y profesionales. Implementar comités de emergencia central y locales, con participación de los y las trabajadores/as. ", unsafe_allow_html=True)
    with st.expander('📖 **Educación**'):
      st.write("<br> **Garantizar el acceso a la educación:** usando la plata del pago de la deuda al FMI", unsafe_allow_html=True)
    with st.expander('♻️ **Ambiente**'):
      st.write("<br> **Eliminar la minería y el uso indiscriminado de agrotóxicos:** rechazar el fracking y la megaminería. Anular el acuerdo YPF-Chevron. Expropiar esas firmas sin indemnización y que reparen los daños causados.<br><br> **Producir y distribuir energía según las necesidades populares fundamentales:** la renta petrolera y minera debe financiar la transición hacia una matriz energética sustentable y diversificada, desarrollando las energías renovables y/o de bajo impacto ambiental en consulta con las comunidades locales. Prohibir las fumigaciones aéreas y el uso indiscriminado de agrotóxicos.", unsafe_allow_html=True)
    with st.expander('👮‍♂️ **Seguridad**'):
      st.write("<br> No se encontraron propuestas en la fuente seleccionada", unsafe_allow_html=True)

    st.write("**Fuente: https://merepresenta.info/propuestas** <br><br>", unsafe_allow_html=True)

#with st.expander("**La Libertad Avanza**"):
    #st.markdown(pdf_display, unsafe_allow_html=True)

#with st.expander("**Juntos por el Cambio**"):
    #st.markdown(pdf_display2, unsafe_allow_html=True)

#with st.expander("**Union por la Patria**"):
    #st.markdown(pdf_display3, unsafe_allow_html=True)

# Load environment variables
load_dotenv()

st.markdown("<h1 style='text-align: center;'>Plataformas electorales nacionales de las agrupaciones politicas<br><br></h1>", unsafe_allow_html=True)

plat1, plat3, plat2 = st.columns([0.4, 0.1, 0.5])

with plat1:
    with st.expander("**La Libertad Avanza**"):
      st.markdown(pdf_display, unsafe_allow_html=True)

    with st.expander("**Juntos por el Cambio**"):
      st.markdown(pdf_display2, unsafe_allow_html=True)

    with st.expander("**Union por la Patria**"):
      st.markdown(pdf_display3, unsafe_allow_html=True)

with plat2:
  
  st.subheader("**Consulta las plataformas electorales con ChatGPT**")

  def main():
      load_dotenv()
      #st.set_page_config(page_title="Consulta las plataformas electorales")
      #st.title("Consulta las plataformas electorales con un chatbot")

      pdf_mapping = {
      'La Libertad Avanza': 'data/LLA.pdf',
      'Juntos por el Cambio': 'data/JxC.pdf',
      'Union por la Patria': 'data/UxP.pdf'
      # Add more mappings as needed
  }
      
      custom_names = list(pdf_mapping.keys())

      selected_custom_name = st.selectbox('Selecciona el PDF', ['', *custom_names])
      pdf = pdf_mapping.get(selected_custom_name)

      # extract the text
      if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
          text += page.extract_text()
          
        # split into chunks
        text_splitter = CharacterTextSplitter(
          separator="\n",
          chunk_size=1000,
          chunk_overlap=200,
          length_function=len
        )
        chunks = text_splitter.split_text(text)
        
        # create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        
        # show user input
        user_question = st.text_input("Pregunta sobre la plataforma electoral:")
        if user_question:
          docs = knowledge_base.similarity_search(user_question)
          
          llm = OpenAI(model_name='gpt-3.5-turbo')
          chain = load_qa_chain(llm, chain_type="stuff")
          with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
            print(cb)
            
          st.write(response)
      

  if __name__ == '__main__':
      main()
