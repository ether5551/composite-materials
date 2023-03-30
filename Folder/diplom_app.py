# -*- coding: utf-8 -*-
"""Diplom_app.ipynb

# Пользовательское приложение для прогнозирования
"""

# Импортируем необходимые библиотеки для нашего приложения
import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, render_template

import pickle

#!pip install tensorflow

app = Flask(__name__, template_folder = 'templates')

model_neuron_path = "my_model_neuron"
html_path = "My_index.html"

# Загружаем модель и определяем параметры функции (всего 12 параметров), 
# попутно преобразуя входгые параметры в необходимую форму для подачи в модель

def set_params(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12):
    print(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12)
    model = keras.models.load_model(model_neuron_path)
    print('done_load')
    mylist = [param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12]
    mylist = np.array(mylist)
    mylist = mylist.reshape(1,-1)
    prediction = model.predict(mylist)
    print('done_pred')
    return prediction[0][0]

@app.route('/', methods=['post', 'get'])

def app_calculation():
    param_lst = []
    message = ''
    max_num = 5.3141436851035
    min_num = 0.547391007365624
    if request.method == 'POST':
        
       # получим данные из наших форм и кладем их в список, который затем передадим функции set_params
        for i in range(1,13,1):
            param = request.form.get(f'param{i}')
            param_lst.append(float(param))
            
        message = set_params(*param_lst)
        # проводим востановление значения из нормальной формы (в диапазоне от 0 до 1) к физическому значению
        message = (message * (max_num - min_num)) + min_num

    # указываем шаблон и прототип сайта для вывода    
    return render_template(html_path, message=message) 

# Запускаем приложение  
app.run()