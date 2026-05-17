from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# List sederhana buat nyimpen tugas
tasks = []

@app.route('/')
def index():
    # Nampilin halaman HTML dan ngirim data tasks
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    # Ngambil inputan dari form HTML
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    # Hapus tugas berdasarkan urutan (index)
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)