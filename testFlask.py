from flask import Flask, request, render_template, redirect
from sorts import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
rows = []
@app.route('/', methods=['post', 'get'])
def index():
    global rows
    n = ''
    time_stamps = {
        'n': '',
        'bubble': '',
        'insert': '',
        'quick': '',
        'merge': '',
        'count': '',
        'type': ''
    }

    if request.method == 'POST':
        n = request.form.get('n')
        typeofarr = request.form.get('type')
        how = request.form.get('how')
        nums = request.form.get('nums')
        print(n)
        if (how == 'rnd'):
            time_stamps['n'] = n
            n = int(n)
            if typeofarr == 'int':
                time_stamps['type'] = 'INT'
                arr = create_rnd_list_int(n)
            else:
                time_stamps['type'] = 'FLOAT'
                arr = create_rnd_list_float(n)
        else:
            time_stamps['n'] = len(nums.split())
            if typeofarr == 'int':
                time_stamps['type'] = 'INT'
                arr = list( map(int, nums.split(' ')) )
            else:
                time_stamps['type'] = 'FLOAT'
                arr = list(map(float, nums.split(' ')))
        #print(arr)
        time_stamps['bubble'] = bubble_sort_time(arr)
        time_stamps['insert'] = insert_sort_time(arr)
        time_stamps['quick'] = quick_sort_time(arr)
        time_stamps['merge'] = merge_sort_time(arr)
        #time_stamps['count'] = count_sort_time(arr)
        rows.append(time_stamps)
        if len(rows) == 6:
            rows = rows[1:]
        return(redirect('/#3'))

    return render_template('index.html', rows = reversed(rows))

@app.route('/book')
def book():
    user_agent = request.headers.get('User-Agent')
    return '<h3> Ur browser is ' + user_agent +' </h3>'
if __name__ == '__main__':
    app.run(debug=True)