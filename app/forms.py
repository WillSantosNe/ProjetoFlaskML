from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange


# Formulário para selecionar o tipo de classificador (tela inicial)
class ClassifierForm(FlaskForm):
    classifier = SelectField('Escolha o Classificador:', choices=[
        ('KNN', 'KNN'),
        ('SVM', 'SVM'),
        ('MLP', 'MLP'),
        ('DT', 'Decision Tree'),
        ('RF', 'Random Forest')
    ])
    submit = SubmitField('Treinar')


# Formulário com os campos do classificador KNN
class KNNForm(FlaskForm):
    n_neighbors = IntegerField('Número de Vizinhos', validators=[DataRequired(), NumberRange(min=1)])
    weights = SelectField('Pesos', choices=[('uniform', 'Uniforme'), ('distance', 'Distância')], default='uniform')
    algorithm = SelectField('Algoritmo', choices=[('auto', 'Auto'), ('ball_tree', 'Ball Tree'), ('kd_tree', 'KD Tree'), ('brute', 'Brute')], default='auto')



# Formulário com os campos do classificador SVM
class SVMForm(FlaskForm):
    C = FloatField('C (Regularização)', validators=[DataRequired(), NumberRange(min=0.1)], default=1.0)
    kernel = SelectField('Kernel', choices=[('linear', 'Linear'), ('rbf', 'RBF'), ('poly', 'Polinomial')], default='rbf')
    degree = IntegerField('Grau (para kernel polinomial)', validators=[NumberRange(min=1)], default=3)
    gamma = SelectField('Gamma', choices=[('scale', 'Scale'), ('auto', 'Auto')], default='scale')



# Formulário com os campos do classificador MLP
class MLPForm(FlaskForm):
    hidden_layer_sizes = StringField('Tamanhos das Camadas Ocultas (e.g. 10,10)', validators=[DataRequired()])
    max_iter = IntegerField('Número Máximo de Iterações', validators=[DataRequired(), NumberRange(min=1)])
    learning_rate_init = FloatField('Taxa de Aprendizado Inicial', validators=[DataRequired(), NumberRange(min=0.0001)], default=0.001)
    solver = SelectField('Solver', choices=[('lbfgs', 'LBFGS'), ('sgd', 'SGD'), ('adam', 'Adam')], default='adam')



# Formulário com os campos do classificador Decision Tree
class DTForm(FlaskForm):
    max_depth = IntegerField('Profundidade Máxima', validators=[NumberRange(min=1)])
    criterion = SelectField('Critério', choices=[('gini', 'Gini'), ('entropy', 'Entropia')], default='gini')
    min_samples_split = IntegerField('Mínimo de Amostras para Divisão', validators=[NumberRange(min=2)], default=2)



# Formulário com os campos do classificador Random Forest
class RFForm(FlaskForm):
    n_estimators = IntegerField('Número de Árvores', validators=[DataRequired(), NumberRange(min=1)])
    max_depth = IntegerField('Profundidade Máxima', validators=[NumberRange(min=1)], default=None)
    criterion = SelectField('Critério', choices=[('gini', 'Gini'), ('entropy', 'Entropia')], default='gini')
    min_samples_split = IntegerField('Mínimo de Amostras para Divisão', validators=[NumberRange(min=2)], default=2)
