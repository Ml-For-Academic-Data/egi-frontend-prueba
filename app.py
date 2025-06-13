from flask import Flask, redirect, request, session, url_for, render_template, flash
from keycloak import KeycloakOpenID
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta más segura

# Configuración para Docker (usa nombres de servicio)
keycloak_openid = KeycloakOpenID(
    server_url="http://host.docker.internal:8081/",  # Nombre del servicio en la red Docker
    client_id="frontend-client",
    realm_name="ML",
    client_secret_key="ZUA1nSULKbOUVSczgFnlN4kKwK7m9YaV"
)

# URLs (desde el navegador usa localhost)
FRONTEND_URL = "http://localhost:3000"
REDIRECT_URI = f"{FRONTEND_URL}/callback"

@app.route("/")
def home():
    if not session.get("access_token"):
        return redirect(url_for("login"))
    
    userinfo = session.get("userinfo", {})
    roles = userinfo.get("resource_access", {}).get("frontend-client", {}).get("roles", [])
    return render_template("index.html", 
                         username=userinfo.get("preferred_username", "Usuario"),
                         email=userinfo.get("email", ""),
                         roles=roles)

@app.route("/login")
def login():
    auth_url = keycloak_openid.auth_url(
        redirect_uri=REDIRECT_URI,
        scope="openid profile email"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        flash("No se recibió código de autorización")
        return redirect(url_for("login"))

    try:
        token = keycloak_openid.token(
            grant_type="authorization_code",
            code=code,
            redirect_uri=REDIRECT_URI
        )
        
        access_token = token.get("access_token")
        session["access_token"] = token.get("access_token")
        session["refresh_token"] = token.get("refresh_token")
        session["id_token"] = token.get("id_token")
        session["userinfo"] = keycloak_openid.userinfo(token["access_token"])

        from jwt import decode  # pip install pyjwt
        decoded_token = decode(access_token, options={"verify_signature": False})
        session["userinfo"] = {
            "resource_access": {
                "frontend-client": {
                    "roles": decoded_token.get("resource_access", {}).get("frontend-client", {}).get("roles", [])
                }
            }
        }
        
        return redirect(url_for("home"))
    
    except Exception as e:
        flash(f"Error de autenticación: {str(e)}")
        return redirect(url_for("login"))

@app.route("/airflow")
def airflow():
    if not session.get("access_token"):
        return redirect(url_for("login"))
    return redirect("http://airflow:8080")  # Nombre del servicio en Docker

@app.route("/panel")
def panel():
    if not session.get("access_token"):
        return redirect(url_for("login"))
    return redirect("http://panel-app:5000")  # Nombre del servicio en Docker

@app.route("/logout")
def logout():
    id_token = session.get('id_token')
    refresh_token = session.get('refresh_token')
    session.clear()
    
    try:
        if refresh_token:
            keycloak_openid.logout(refresh_token)
        
        logout_url = (
            f"http://localhost:8081/realms/ML/protocol/openid-connect/logout?"
            f"post_logout_redirect_uri={FRONTEND_URL}"
        )

        if id_token:
            logout_url += f"&id_token_hint={id_token}"

        return redirect(logout_url)
        
    except Exception as e:
        print(f"Error en logout: {str(e)}")
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)