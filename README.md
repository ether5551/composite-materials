# composite-materials
## Работа по композитным материалам в ходе выполнения ВКР по курсам

1).	В процессе исследования изучены теоретические основы и методы решения поставленной задачи.

Спрогнозировать по входным параметрам ряд конечных свойств получаемых композиционных материалов при следующих используемых признаках: 

•	Соотношение матрица-наполнитель
    
•	Плотность, кг/м3
    
•	Модуль упругости, ГПа
    
•	Количество отвердителя, м.%
    
•	Содержание эпоксидных групп,%_2
    
•	Температура вспышки, С_2
    
•	Поверхностная плотность, г/м2
    
•	Потребление смолы, г/м2
    
•	Прочность при растяжении, МПа
    
•	Потребление смолы, г/м2
    
•	Угол нашивки, град
    
•	Шаг нашивки
    
•	Плотность нашивки
    
2)	Ознакомление с элементами, составляющими композитные материалы.	
3)	Проведен разведочный анализ и представлена визуализация предложенных данных. Представлены гистограммы распределения каждой из переменной, диаграммы ящика с усами, попарные графики рассеяния точек. В таблице представлены для каждой колонки среднее, медианное значение, проведен анализ и исключены выбросы, проверена выборка на наличие пропусков.	
4)	Проведена предобработка данных (удалены шумы, нормализация и т.д.).	
5)	Обучено нескольких моделей для прогноза модуля упругости при растяжении и прочности при растяжении.
6)	Написаны 2 нейронные сети, которые будет рекомендовать соотношение "матрица-наполнитель".
7)	Разработано пользовательское приложение на Flask, выдаваемое прогноз (Выходные данные (прогнозируемы) - Соотношение "матрица - наполнитель").
8)	Оценена точность модели на тренировочном и тестовом датасете.
9)	Создан репозиторий в GitHub и размещен код исследования.
10) Оформлен данный файл README.

## Структура репозитория:

Folder - папка с пользовательским приложением и всем для него необходимым

Folder/my_model_neuron - сохранённая нейронная модель

Folder/templates - папка с html документом загружаемой страницы flask приложения

Diplom.ipynb - ноутбук с проектом и всеми расчётами

Folder/diplom_app.py - программа с простым flask приложением

README.md - текстовый документ с основной информацией по выгруженным документам и общей информацией по разрабатываемому проекту

model_E.pkl - сохранёная модель для определения параметра "Модуль упругости при растяжении, ГПа"

model_S.pkl - сохранёная модель для определения параметра "Прочность при растяжении, МПа"

## Инструкция использования приложения:

Приложение позволяет решать задачу прогнозирования "Соотношение матрица наполнитель". Для получения прогноза необходимо:

1) Запустить diplom_app.py

2) В появившейся строке ( * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)) - нажать на ссылку: http://127.0.0.1:5000/

3) В новом открывшемся окне (сайте) ввести 12 входных параметров и нажать на кнопку "Получить рекомендацию"

4) Ниже появится результат в виде числа с плавающей точкой
