
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import post  # Importa el modelo post definido en models.py
from .formulario import FormularioPost  # Importa el formulario para crear/editar posts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Formularios de creación de usuario e inicio de sesión
from django.contrib.auth.models import User  # Modelo de usuario de Django
from django.contrib.auth import login, logout, authenticate  # Funciones de autenticación y gestión de sesión
from django.contrib.auth.decorators import login_required  # Decorador que exige que el usuario esté autenticado

# Vistas del proyecto Django

def home(request):
    """Página de inicio que muestra todos los posts."""
    posts = post.objects.all()  # Consulta todos los posts de la base de datos
    return render(request, 'index.html', {
        'posteos': posts  # Envía la lista de posts a la plantilla index.html
    })


def about(request):
    """Página estática 'Acerca de'."""
    return render(request, 'about.html')


def posts(request):
    """Vista para listar todos los posts en una página independiente."""
    posts = post.objects.all()  # Consulta todos los posts
    return render(request, 'posts.html', {
        'posteos': posts  # Pasa los posts al contexto de la plantilla
    })


def post_create(request):
    """Crea un nuevo post mediante un formulario.

    - GET: muestra el formulario de creación.
    - POST: valida los datos, asigna autor y guarda el post en la BD.
    """
    if request.method == "GET":
        # Muestra el formulario vacío para crear un post nuevo
        return render(request, 'crearPost.html', {"formularioPost": FormularioPost})
    else:
        try:
            # Crea el formulario con los datos enviados en POST
            form = FormularioPost(request.POST)
            # No guarda todavía la instancia en la BD para añadir el autor
            nuevoPost = form.save(commit=False)
            nuevoPost.autor = request.user  # Asigna el usuario actual como autor
            nuevoPost.save()  # Guarda el post completo en la base de datos
            return redirect('posts_list')  # Redirige a la lista de posts
        except:
            # En caso de error vuelve a mostrar el formulario con un mensaje de error
            return render(request, 'crearPost.html', {"formularioPost": FormularioPost, "error": "Error al crear"})


@login_required
def post_detail(request, post_id):
    """Muestra el detalle de un post específico.

    Requiere que el usuario esté autenticado para ver el detalle.
    """
    # Busca el post por su ID; si no existe devuelve error 404
    post_detail = get_object_or_404(post, id=post_id)
    return render(request, 'detallePost.html', {
        'post': post_detail  # Pasa el post encontrado a la plantilla
    })


def post_edit(request, post_id):
    """Edita un post existente.

    - GET: muestra el formulario con los datos actuales del post.
    - POST: guarda los cambios y redirige a la lista.
    """
    post_detail = get_object_or_404(post, id=post_id)  # Obtiene el post a editar
    if request.method == 'POST':
        formulario = FormularioPost(request.POST, instance=post_detail)
        formulario.save()  # Guarda los cambios en el post existente
        return redirect('posts_list')
    else:
        formulario = FormularioPost(instance=post_detail)  # Crea el formulario con los datos actuales

    return render(request, 'editarPost.html', {'formulario': formulario, 'post': post_detail})


def post_delete(request, post_id):
    """Elimina un post específico.

    Solo borra el post cuando la solicitud es POST.
    """
    post_detail = get_object_or_404(post, id=post_id)
    if request.method == 'POST':
        post_detail.delete()  # Elimina el post de la base de datos
        return redirect('posts_list')


def register(request):
    """Registra un nuevo usuario.

    - GET: muestra el formulario de registro.
    - POST: valida contraseñas y crea el usuario.
    """
    if request.method == 'GET':
        return render(request, 'registro.html', {
            "formularioRegister": UserCreationForm()
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Intenta buscar un usuario con el mismo nombre
                User.objects.get(username=request.POST["username"])
                return render(request, 'registro.html', {
                    "formularioRegister": UserCreationForm(),
                    "error": "El nombre de usuario ya está en uso."
                })
            except User.DoesNotExist:
                # Si no existe, crea el nuevo usuario y lo guarda
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)  # Inicia sesión con el usuario recién creado
                return redirect('posts_list')

        # Si las contraseñas no coinciden muestra error
        return render(request, 'registro.html', {
            "formularioRegister": UserCreationForm(),
            "error": "Las contraseñas no coinciden."
        })


def login_view(request):
    """Inicia sesión de un usuario.

    - GET: muestra el formulario de login.
    - POST: autentica y redirige al home si es exitoso.
    """
    if request.method == 'GET':
        return render(request, 'login.html', {"formularioLogin": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                "formularioLogin": AuthenticationForm,
                "error": "Usuario o contraseña incorrectos."
            })

        login(request, user)  # Inicia sesión del usuario autenticado
        return redirect('home')


def logout_view(request):
    """Cierra la sesión del usuario activo y redirige al login."""
    logout(request)
    return redirect('login')
    