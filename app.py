import streamlit as st

st.set_page_config(
    page_title="servidor",
    page_icon="https://cdn-icons-png.flaticon.com/128/5863/5863644.png",
    layout="wide"
)

# Inyectar CSS personalizado
st.markdown(
    """
    <style>
    /* Cambiar el fondo del sidebar */
    [data-testid="stSidebar"] {
        background-image: url("https://i.ibb.co/pL04hNG/Sin-t-tulo-2160-x-3840-px.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/128/9792/9792988.png")
    st.header(":blue[Integrantes]",divider="gray")
    st.write("• Andrés Felipe Ramírez Mackenzie")
    st.write("• Keiner Zuñiga Romero")
    st.write("• Mateo Villarreal Garnica")
    st.write("• Salomon Garcia Reyes")


st.header("Bienvenidos",divider="blue")
st.write("Este proyecto de redes y comunicaciones se enfoca en la implementación de un servidor utilizando Windows Server 2022, con estaciones de trabajo configuradas en Windows 7 como clientes. El objetivo es demostrar la instalación y configuración de un entorno de red funcional, optimizando la conectividad y el manejo de servicios a través de un servidor centralizado.")

st.subheader("Configuracion para la instalacion de windows server",divider="blue")
with st.expander("ver capturas de el procedimiento👇"):
    
    st.subheader("Inicar instalacion")
    st.image("instalar.png")
    st.write("""
        Al configurar la maquina virtual del windows server no cargamos la iso, solo ponemos el nombre personalizado y elejimos la version de 2022
        """)
    
    st.subheader("Desactivar disquete")
    st.image("disquete.png")
    st.write("""
        Desactivamos la opcion de disquete en las configuraciones virtual box de windows server 
        """)
    st.subheader("Subir iso de el windows server")
    st.image("subir_iso.png")
    st.write("""
        Cargamos la iso de windows server despues de realizaer las configuraciones, ya que el inicio no se cargo
        """)
    
    st.subheader("Red adaptador puente")
    st.image("red_puente.png")
    st.write("""
        Activamos red de adaptdor puente en el server y el windows 7 para que tenga una correcta conexion
        """)
    

st.subheader("Conexion entre server y cliente",divider="blue")
st.video("https://youtu.be/sXWZtNF2ysQ?si=6JRXISVbwzk88k2d")
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
    Aquí para poder realizar la conexion es importante tener los pings que se utilizaran
    a la mano mediante CMD. Una vez hagamos esto entramos a nuestro panel de control luego a centro 
    de redes (Tanto en el servidor como en el windows que esté ocupando en el momento), luego, realizaremos
    una desactivacion de firewall (repitiendo esto en el server y el windows de uso). Una vez hecho esto
    abriremos nuestro CMD y así ingresamos nuestros pings en en el CMD hasta completar el proceso.
    """)

st.subheader("Instalacion ADS y LDS",divider="blue")
st.video("https://youtu.be/GyEPgMxbD-Q?si=7eM-gF8rQRCJ99Jz")
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
    Una vez completemos la conexión, procederemos a asignar roles en nuestro servidor
    (importante asignar los ADS y LDS) y al finalizar con la asignación instalaremos nuestros roles seleccionados. Nuestra 
    maquina necesitará un reinicio para poder completar el proceso de instalaciones. 
    """)

st.subheader("Configuracion de dominio",divider="blue")
st.video("https://youtu.be/WyAD8ibzA6g?si=u3UE-TGICA6XAKB1")
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
    Una vez completado el reinicio podremos ver en la barra de navegación una alerta. Aqui procederemos con nuestro
    siguiente paso y es el dominio. Aquí haremos un renombrado con nuestro nombre de preferencia, haremos una creación de 
    contraseña y empezaremos a crear nuestro DNS. Ya completado esto nos retornará un nombre de manera automatica que pasará a 
    ser nuestro nombre de "dominio" o "Administrator", al recibir esto ya pasaremos a la instalación final donde deberemos realizar
    otro reincio de la maquina.
    """)

st.subheader("Conexion cliente con dominio",divider="blue")
st.video("https://youtu.be/3FUdtlLfpwI?si=TvCZh8JE72o_yu06")
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
    Realizado el reinicio, buscaremos en nuestro Windows de usuario el apartado de sistema, se coloca nuestro nombre de dominio (.local)
    usaremos nuestro nombre de usuario (0\Administrator) y nuestra contraseña de administrador, hecho esto se necesitará realizar un reinicio 
    para poder aplicar los cambios. En nuestro windows server, debemos irnos a el apartado de herramientas seguido de esto "Usuarios y computadores"
    y ahí podremos visualizar nuestras maquinas conectadas a nuestro server.
    """)

st.subheader("Creacion de carpeta compartida(manera 1)",divider="blue")
st.video("https://youtu.be/VHL3TabD0ek?si=NlE0NsYM0lrJzV9H")
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
    Aqui se creará la carpeta en el Windows server y se le agregará unas propiedades con el fin de hacer una comparticion de acceso a los usuarios
    seguido de eso, se realizará el compartido con el windows de uso donde deberemos acceder a el explorador de archivos, el nombre de nuestro dispositivo
    y podremos visualizar nuestra carpeta tanto en el windows de uso como en el server realizando varios archivos de texto donde se escriben pequeñas frases 
    para que quede en claro, que no solo manda archivos, sino que este mismo tambien permite cambiar el contenido de este archivo en "tiempo real". Así 
    concluyendo con exito nuestro servidor usando Windows 7 Pro y Windows Server 2022.
        """)


st.subheader("Creacion de usuarios",divider="blue")
st.video("https://youtu.be/O531e_XevOo?si=h6hCMlW27mEyaUZv")
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
        Entramos a las herramientas de e administrador del servidor y nos vamos al aparta del directorio activo
        en la carpeta de users vamos a crear un nuevo usuario, dandole un nombre y su respectiva contraseña, podemos elegir una opcion para que el usuario cambie su contraseña una ves ingrese pero en este caso 
        no es necesario. Luego de crear el usuairio en Windows server nos dirigimos a windows 7 
        y ingresamos con otra cuenta y ponemos la que creamos anteriormente.
        """)

st.subheader("Compartir carpetas por usuairos",divider="blue")
st.video("https://www.youtube.com/watch?v=AHkYmK2nXKU&list=PLGLrW3nmk_i5E7PUtmWEWu3w0D_6_2WKY&index=8")
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
        En este paso vamos a compartir una carpeta con el mismo administrador de servidor como se mostro en 
        videos anteriores, solo que esta vez en lugar de elegir gruó users vamos a seleccionar el o los usuarios especificos, para que solo le salgan los archivos compartidos con ellos. Recordemos que debemos deshabilitar compartir los subfolders para que solo se comparta el principal.
        """)

st.subheader("Conexion server linux",divider="blue")
st.video("https://youtu.be/32UOj2R9FJY?si=KAjBuwvBl8gPmQlv")
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
        En este paso vamos a verificar la conexion de linux con nuestro servidor de windows server, para eso debemos tener el IP de linux(ubunto 24.10) ponemos un IP que este en el mismo rango que el server para este caso es 192.168.20.22 y como ruta por defecto ponemos el IP de windows server y para verificar hacemos ping al IP y al nombre del dominio
        """)
