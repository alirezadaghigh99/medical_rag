from flask import Flask, render_template, request, session, redirect, url_for

from app.components.retriever import create_qa_chain

from dotenv import load_dotenv
import os

from app.common.logger import get_logger
from app.common.custom import CustomException

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")

app = Flask(__name__)
app.secret_key = os.urrandom(24).hex()

logger = get_logger(__name__)

from markupsafe import Markup
def nl2br(value):
    """Convert newlines to <br> tags."""
    return Markup(value.replace("\n", "<br>\n"))

app.jinja_env.filters['nl2br'] = nl2br
@app.route('/', methods=['GET', 'POST'])
def index():
    
    if "message" not in session:
        session["message"] = ""
    
    if request.method == 'POST':
        user_input = request.form.get("prompt", "").strip()
        
        if user_input:
            message = session.get("message", "")
            message.append({"role": "user", "content": user_input})
            session["message"] = message
            
            try:
                qa_chain = create_qa_chain()
                response = qa_chain.invoke(user_input)
                
                result = response.get("result", "")
                if result:
                    message.append({"role": "assistant", "content": result})
                    session["message"] = message
                else:
                    session["message"].append({"role": "assistant", "content": "No answer found."})
            except CustomException as ce:
                logger.error(f"Custom exception occurred: {ce}")
                session["message"].append({"role": "assistant", "content": str(ce)})
                return render_template('index.html', messages=session["message"])
        return redirect(url_for('index'))
    return render_template('index.html', messages=session["message"])
                
@app.route('/clear')
def clear():
    """Clear the session messages."""
    session.pop("message", None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        logger.error(f"An error occurred while starting the Flask application: {e}")
        raise CustomException("Failed to start the Flask application.", e)