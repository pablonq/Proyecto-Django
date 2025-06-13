
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import post # Importa el modelo post
from .formulario import FormularioPost # Importa el formulario para post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Importa el formulario de autenticación
from django.contrib.auth.models import User # Importa el modelo de usuario
from django.contrib.auth import login, logout, authenticate # Importa el método de inicio de sesión
from django.contrib.auth.decorators import login_required # Importa el decorador para requerir autenticación

# Create your views here.
def home(request):
   posts = post.objects.all()  # Obtiene todos los posts de la base de datos
   return render(request, 'index.html',{
        'posteos': posts  # Pasa los posts al contexto de la plantilla
    })

def about(request):
    return render(request, 'about.html')

def posts(request):
    posts = post.objects.all()  # Obtiene todos los posts de la base de datos
    return render(request, 'posts.html',{
        'posteos': posts  # Pasa los posts al contexto de la plantilla
    })  

@login_required  # Requiere que el usuario esté autenticado para acceder a esta vista
def post_create(request):
    if request.method == "GET":
        return render(request, 'crearPost.html', {"formularioPost": FormularioPost})
    else:
        try:
            form = FormularioPost(request.POST)
            nuevoPost = form.save(commit=False)
            nuevoPost.autor = request.user
            nuevoPost.save()
            return redirect('posts_list')  # Redirige a la lista de posts después de crear uno nuevo
        except:
            return render(request, 'crearPost.html', {"formularioPost": FormularioPost, "error": "Error al crear"})

@login_required  # Requiere que el usuario esté autenticado para acceder a esta vista

def post_detail(request, post_id):
    post_detail = post.objects.get(id=post_id)  # Obtiene el post por su ID
    #post_detail = get_object_or_404(post, id=post_id)  # Obtiene el post por su ID
    
    return render(request, 'detallePost.html', {
        'post': post_detail,  # Pasa el post al contexto de la plantilla
        
    })
    
def post_edit(request, post_id):
    post_detail = get_object_or_404(post, id=post_id)  # Obtiene el post por su ID
    if request.method == 'POST':
        formulario = FormularioPost(request.POST, instance=post_detail)  # Crea un formulario con el post existente 
        formulario.save()  # Guarda el formulario
        return redirect('posts_list')  # Redirige a la lista de posts
    else:
        formulario = FormularioPost(instance=post_detail)
    return render(request, 'editarPost.html', {'formulario': formulario, 'post': post_detail})
    
def post_delete(request, post_id):
    post_detail = get_object_or_404(post, id=post_id)  # Obtiene el post por su ID
    if request.method == 'POST':
        post_detail.delete()  # Elimina el post
        return redirect('posts_list')  # Redirige a la lista de posts
    
def register(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            "formularioRegister": UserCreationForm()
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Intenta obtener el usuario, si existe lanza error
                User.objects.get(username=request.POST["username"])
                # Si el usuario existe, muestra un error
                return render(request, 'registro.html', {
                    "formularioRegister": UserCreationForm(),
                    "error": "El nombre de usuario ya está en uso."
                })
            except User.DoesNotExist:
                # Si el usuario no existe, lo crea
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)  # Inicia sesión con el nuevo usuario
                return redirect('posts_list')
        # Si las contraseñas no coinciden
        return render(request, 'registro.html', {
            "formularioRegister": UserCreationForm(),
            "error": "Las contraseñas no coinciden."
        })

def login_view(request):  
    if request.method == 'GET':
        return render(request, 'login.html', {"formularioLogin": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"formularioLogin": AuthenticationForm, "error": "Usuario o contraseña incorrectos."})

        login(request, user)
        return redirect('home')  # Redirige a la lista de posts si el inicio de sesión es exitoso

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige a la página de inicio
    