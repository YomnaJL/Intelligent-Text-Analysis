from flask import Flask, request, render_template # render_template est la nouveauté
import time
from services import process_text # On importe notre fonction !

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    response_time = None
    
    if request.method == "POST":
        text = request.form.get("text", "")
        lang_choice = request.form.get("lang", "fr")
        task = request.form.get("task", "summary")
        
        if text.strip():
            start_time = time.time()
            # C'est ici qu'on appelle la fonction depuis l'autre fichier
            result = process_text(text, lang_choice, task)
            response_time = time.time() - start_time
        else:
            result = "❗ Veuillez entrer un texte à traiter."
            
    # On utilise maintenant render_template pour charger le fichier index.html
    return render_template("index.html", result=result, response_time=response_time)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)