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
    st.write("• Andrés Felipe Ramírez Mackenzie ")
    st.write("• Keiner Zuñiga Romero ")
    st.write("• Mateo Villarreal Garnica ")
    st.write("• Salomon Garcia Reyes")




st.header("Bienvenidos",divider="blue")
st.write("Este proyecto de redes y comunicaciones se enfoca en la implementación de un servidor utilizando Windows Server 2022, con estaciones de trabajo configuradas en Windows 7 como clientes. El objetivo es demostrar la instalación y configuración de un entorno de red funcional, optimizando la conectividad y el manejo de servicios a través de un servidor centralizado.")

st.subheader("Configuracion para la instalacion de windows server",divider="blue")
with st.expander("ver capturas del procedimiento👇"):
    
    st.subheader("Inicar instalacion")
    st.image("instalar.png")
    st.write("""
        Al configurar la maquina virtual del windows server no cargamos la iso, solo ponemos el nombre personalizado y elejimos la version de 2022, ya mas adelante subirimos la iso del server.
        """)
    
    st.subheader("Desactivar disquete")
    st.image("disquete.png")
    st.write("""
        Desactivamos la opcion de disquete en las configuraciones virtual box de windows server, esto se hace para que aranque de manera directa con el disco
        """)
    st.subheader("Subir iso de el windows server")
    st.image("subir_iso.png")
    st.write("""
        Cargamos la iso de windows server despues de realizaer las configuraciones, ya que el inicio no se cargo, la buscamos en nuestros archivos
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

st.header("Conexion fisica",divider="violet")
st.subheader("Cables ethernet")
st.image("collage cable.jpg",use_column_width=True)
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
        Comenzando con la parte física, se prepararon cables UTP de categoría 6, lo recomendado es utilizar cables de categoría 5e o superior.
        Se utilizaron un total de 4 metros de cable y 6 conectores RJ45. Los cables fueron ponchados, y luego se fabricaron dos cables con doble conexión RJ45, 
        que van del patch panel al switch de red. Los otros dos cables fueron pelados, pero solo se ponchó un extremo de cada uno;
        estos cables conectan la parte trasera del patch panel con los portátiles.
        """)
    
st.subheader("Kit de trabajo")
st.image("kit.jpg",use_column_width=True)
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""
        """)

st.subheader("Patch panel")
st.image("panel.jpg",use_column_width=True)
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""Este es un dispositivo que nos ayudará a la realización de las conexión y las distribuciones de los cables
            sirve para la gestion de cables de red, permitiendo conexiones faciles y ordenadas. Su organización ayuda a mantener un área
            de trabajo limpia y ordenada y con ayuda de una ponchadora de impacto metemos los cables de en el orden o la organización
            de los cables, en este caso, nosotros usamos la organización tipo B.""")

st.subheader("Prueba de conexion")
st.image("cap.jpg",use_column_width=True)
with st.expander("Haz clic para ver la descripción 👇"):
    st.write("""Se realizará la conexion final, cabe resaltar que al usar dos equipos uno debe usar el Windows server 2020 y el otro el Windows 7,
            el portador de windows 7 debe ser añadido al dominio del server, mediante el apartado de sistemas y poniendo el DNS igual al del server. Una vez completados todos los pasos
            ya el cliente se unirá a el servidor y se hará una prueba creando una carpeta que solo lo pueda ver el cliente. Cabe resaltar que debes modificar los permisos para que solo 
            el cliente pueda verla, ya despues de esto se creará un archivo de texto (Lo mas simple de hacer) y se deberá mostrar en el cliente e igual el cliente puede modificar
            y añadir carpetas y se debe mostrar en el server.""")
