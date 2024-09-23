from functools import wraps

# Simula um estado de autenticação do usuário
USER_AUTHENTICATED = True

def requires_authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not USER_AUTHENTICATED:
            print("Acesso negado. Usuário não autenticado.")
            return
        return func(*args, **kwargs)
    return wrapper

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Chamada da função: {func.__name__} com args: {args} e kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Função {func.__name__} retornou {result}")
        return result
    return wrapper

@log_calls
@requires_authentication
def get_user_profile(user_id):
    print(f"Buscando perfil do usuário {user_id}")
    return {"user_id": user_id, "name": "Alice"}

@log_calls
@requires_authentication
def update_user_profile(user_id, new_data):
    print(f"Atualizando perfil do usuário {user_id} com {new_data}")
    return {"user_id": user_id, "updated_data": new_data}

# Chamando as funções
print("-------------------")
profile = get_user_profile(1)
print(profile)

print("-------------------")
update_result = update_user_profile(1, {"name": "Alice Smith"})
print(update_result)
