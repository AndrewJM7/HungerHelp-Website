from blog.forms import RecipeForm, images
from models import Post
from flask import Blueprint, render_template, redirect, url_for, send_from_directory
from app import db, app

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')


@app.route("/images/images/<filename>")
def get_file(filename):
    return send_from_directory('images/images', filename)


@blog_blueprint.route('/blog', methods=['GET', 'POST'])
def blog():
    form = RecipeForm()
    if form.validate_on_submit():

        image_name = images.save(form.image.data)
        image_url = url_for("get_file", filename=image_name)

        new_post = Post(title=form.title.data,
                        recipe=form.recipe.data,
                        ingredients=form.ingredients.data,
                        image=image_url,
                        price=form.price.data)

        # add the new recipe to the database
        db.session.add(new_post)
        db.session.commit()

        return render_template('/blog/blog.html', form=form, file_url=image_url)

    return render_template('/blog/blog.html', form=form)


@blog_blueprint.route('/blog_home', methods=['GET','POST'])
def blog_home():
    recipes = Post.query.all()
    print(recipes)
    if recipes:
        return render_template('blog/blog_home.html', recipes=recipes)

    return render_template('blog/blog_home.html')






