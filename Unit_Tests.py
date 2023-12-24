class Usuarioprueba:
    def __init__(self,nombre,email,edad):
       self.nombre = nombre
       self.email = email
       self.edad = edad
       
    def obtener_nombre(self):
           return self.nombre
       
    def obtener_edad(self):
        return self.edad
    
    def obtener_email(self):
        return self.email
       
       
       
       
class Comentarioprueba:
    
    def __init__(self,autor,texto,post):
       self.autor = autor
       self.texto = texto
       self.post = post
       
    def obtener_autor(self):
           return self.autor
       
    def obtener_texto(self):
        return self.texto
    
    def obtener_post(self):
        return self.post
        




class Videoprueba:
    
    def __init__(self,autor_video,video_url,categoria):
       self.autor_video = autor_video
       self.video_url = video_url
       self.categoria = categoria
       
    def obtener_autor_video(self):
           return self.autor_video
       
    def obtener_video_url(self):
        return self.video_url
    
    def obtener_categoria(self):
        return self.categoria
       

#PRUEBAS CLASE COMENTARIOPRUEBA

comentario = Comentarioprueba("RicardoIorioV8","se vos, nomas","concierto river plate")
autor = comentario.obtener_autor()
texto = comentario.obtener_texto()
post = comentario.obtener_post()



def conseguir_autor():
    if autor == "martin123":
        print("prueba fallida") 
    elif autor == "RicardoIorioV8":
        print("prueba exitosa")
    else:
        print("prueba fallida") 
    

    
def conseguir_texto():
    if texto == "me olvide la letra la....":
        print("prueba fallida")
    elif texto == "se vos, nomas":
        print("prueba exitosa")
    else:
        print("prueba fallida")
    


def conseguir_post():
    if post == "concierto velez sarsfield":
        print("prueba fallida")
    elif post == "concierto river plate":
        print("prueba exitosa")
    else:
        print("prueba fallida")        


#PRUEBAS CLASE USUARIOPRUEBA

user = Usuarioprueba("mario","m@a.com",20)
nombre = user.obtener_nombre()
edad = user.obtener_edad()
email = user.obtener_email()



def conseguir_edad():
    if edad >= 18:
        print("prueba exitosa") 
    else: 
        print("prueba fallida") 
    

    
def conseguir_nombre():
    if nombre == "mario":
        print("prueba exitosa")
    else:
        print("prueba fallida")
    


def conseguir_email():
    if email == "m@a.com":
        print("prueba exitosa")
    else:
        print("prueba fallida")
        
        
#PRUEBAS CLASE VIDEOPRUEBA

video = Videoprueba("toto goransky","media/video_toto_honu_beach.mp4","surf")
autor_video = video.obtener_autor_video()
video_url = video.obtener_video_url()
categoria = video.obtener_categoria()



def conseguir_autor_video():
    if autor_video != "toto goransky":
        print("prueba fallida") 
    else: 
        print("prueba exitosa") 
    

    
def conseguir_video_url():
    if video_url == "avatares/avatar_predeterminado.webp":
        print("prueba fallida")
    elif video_url == "media/video_toto_honu_beach.mp4":
        print("prueba exitosa")
    else:
        print("prueba fallida")
    


def conseguir_categoria():
    if categoria == "surf".capitalize():
        print("prueba fallida")
    elif categoria == "surf".upper():
        print("prueba fallida")
    elif categoria == "surf":
        print("prueba exitosa")
    else:
        print("prueba fallida")


print("PRUEBAS COMENTARIO")
conseguir_autor()
conseguir_texto()
conseguir_post()
print("PRUEBAS USUARIO")
conseguir_edad()
conseguir_nombre()
conseguir_email()
print("PRUEBAS VIDEO")
conseguir_autor_video()
conseguir_video_url()
conseguir_categoria()
