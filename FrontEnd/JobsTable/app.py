# app.py


from flask import Flask, render_template, request, redirect, url_for
from models import db, Job

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
db.init_app(app)



with app.app_context():
    db.create_all()

@app.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

# app.py

# ... (previous code) ...

# app.py

# ... (previous code) ...

from flask import abort

# ... (previous code) ...

@app.route('/delete_job/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    job = Job.query.get(job_id)

    if not job:
        abort(404)  # Handle job not found

    db.session.delete(job)
    db.session.commit()

    return redirect(url_for('index'))

# ... (rest of the code) ...


# ... (rest of the code) ...



# app.py

# ... (previous code) ...

@app.route('/update_job/<int:job_id>', methods=['GET', 'POST'])
def update_job(job_id):
    job = Job.query.get(job_id)

    if request.method == 'POST':
        job.title = request.form['title']
        job.description = request.form['description']
        job.requirements = request.form['requirements']
        job.hours = request.form['hours']

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('update_job.html', job=job)

# ... (rest of the code) ...


@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        requirements = request.form['requirements']
        hours = request.form['hours']

        new_job = Job(title=title, description=description, requirements=requirements, hours=hours)

        db.session.add(new_job)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('post_job.html')

if __name__ == '__main__':
    app.run(debug=True)
