from flask import Flask, request, render_template
from route import search_dijkstra, search_sales

app = Flask(__name__, static_folder='static')


temple_list = ['鹿苑寺（金閣寺）', '南禅寺', '鞍馬寺', '慈照寺（銀閣寺）', '清水寺', '八坂神社','本願寺（西本願寺）', '天龍寺', '西芳寺（苔寺）', '宇治上神社']
pos_list = [[35.03937, 135.729243],
            [35.011245, 135.793802],
            [35.11790708, 135.77052644],
            [35.027021, 135.798206],
            [34.994856, 135.785046],
            [35.003634, 135.778526],
            [34.991381, 135.751672],
            [35.015853, 135.67369],
            [34.991964, 135.683309],
            [34.892068, 135.81143]]

temples_dict = {temple: pos for temple, pos in zip(temple_list, pos_list)}

@app.route('/')
def index():
    return render_template('/html/index.html')
            
@app.route('/yorimiti', methods=['GET', 'POST'])
def dijkstra():
    result = []
    select_dict = {}
    message=""

    if request.method == 'POST' and "spot" in request.form:
        # 同じものが選ばれている場合の処理が必要
        start, goal = request.form.getlist('spot')
        if start != goal:
            result = search_dijkstra(start, goal)
            select_dict = {name: temples_dict[name] for name in result}
            message = "検索結果を表示します"
        else:
            message = "スタート地点とゴール地点には異なる地名を選んでください"
    return render_template('/html/dijkstra.html', result=result, message=message, select_dict=select_dict)


@app.route('/route', methods=['GET', 'POST'])
def sales():
    result = []
    select_dict = {}
    message=""
    time=""

    if request.method == 'POST' and "spots" in request.form:
        # 同じものが選ばれている場合の処理が必要
        result_data = request.form.getlist('spots')
        if len(set(result_data)) == 4:
            result, time = search_sales(result_data)
            select_dict = {name: temples_dict[name] for name in result}
            message = "検索結果を表示します"
        else:
            message = "各観光地に異なる地名を選んでください"
    return render_template('/html/sales.html', result=result, message=message, time=time, select_dict=select_dict)

@app.route("/map")
def mapview(result):
    print(result)
    select_dict = {name: temples_dict[name] for name in result}
    return render_template('/html/map.html', result=result, select_dict=select_dict)