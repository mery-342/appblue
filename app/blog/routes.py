from flask import render_template
from app.blog import blog_bp

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    return render_template('blog/entrada.html', id_entrada=id)